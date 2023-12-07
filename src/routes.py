"""Directs user to different parts of the website"""
import tempfile
import os
from io import BytesIO
from flask import redirect, render_template, request, make_response
from flask_app import app
from services.bibtex_service import BibTextService
from repositories.citation_repository import CitationRepository
from database import db


citation_repo = CitationRepository(db)
bibtex_service = BibTextService()

# implement later if want, requires "secretkey" in env
"""
def error(message, destination):
    print("awadsadasdsa")
    flash(message)
    return redirect(destination)
"""
@app.route("/")
def index():
    citation_data = citation_repo.get_citations()
    bibtex_data = bibtex_service.get_references_in_bibtex_format(citation_data)
    show_bibtex = request.args.get("show_bibtex")

    return render_template("index.html", references=citation_data,
                           references_bibtex=bibtex_data, show_bibtex=show_bibtex)

@app.route("/add_reference", methods=["POST"])
def add_reference():
    reference_type = request.form["reference_type"]
    reference_id = request.form["ID"]
    author = request.form["author"]
    title = request.form["title"]
    year = request.form["year"]
    citation_repo.create_citation(reference_type, reference_id, author, title, int(year))
    bibtex_service.write_to_bib_file(reference_type, reference_id, author, title, year)

    return redirect("/")

@app.route("/delete_reference/<reference_id>", methods=["POST"])
def delete_reference(reference_id):
    bibtex_data = bibtex_service.read_from_bib_file()
    bibtex_service.delete_from_bib_file(reference_id, bibtex_data)
    citation_repo.delete_citation(reference_id)
    return redirect("/")

@app.route("/delete_references", methods=["POST"])
def delete_all_references():
    bibtex_service.delete_all_from_bib_file()
    citation_repo.delete_all_citations()

    return redirect("/")


@app.route("/download_references", methods=["POST"])
def download_references():
    citation_data = citation_repo.get_citations()
    bibtex_data = bibtex_service.get_references_in_bibtex_format(citation_data)
    with tempfile.NamedTemporaryFile('w', delete=False) as temp_file:
        temp_file.write('\n'.join(bibtex_data))

    file_content = BytesIO()
    with open(temp_file.name, 'r', encoding='utf-8') as file:
        file_content.write(file.read().encode('utf-8'))

    response = make_response(file_content.getvalue())
    response.headers.set('Content-Disposition', 'attachment', filename='references.bib')
    response.headers.set('Content-Type', 'application/bibtex')

    os.unlink(temp_file.name)
    return response

@app.route('/register', methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password_hash"]

        if citation_repo.create_user(username, password):
            return redirect("/")
        return redirect("/register")
            # return error("Registeration failed, user already exists", "register")
    return redirect("/")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password_hash"]
        if citation_repo.login_user(username, password):
            return redirect("/")

        return redirect("/login")
            #return error("Wrong username or password", "login")
    return redirect("/")
