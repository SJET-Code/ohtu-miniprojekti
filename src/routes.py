"""Directs user to different parts of the website"""
import tempfile
import os
from io import BytesIO
from flask import redirect, render_template, request, make_response, flash
from flask_app import app
from services.bibtex_service import BibTextService
from repositories.citation_repository import CitationRepository
from repositories.user_repository import UserRepository
from database import db


citation_repo = CitationRepository(db)
user_repo = UserRepository(db)
bibtex_service = BibTextService()


def error(message, destination):
    flash(message)
    return redirect(destination)

@app.route("/")
def index():
    if user_repo.is_user():
        citation_data = citation_repo.get_citations(user_repo.user_id())
        bibtex_data = bibtex_service.get_references_in_bibtex_format(citation_data)
        show_bibtex = request.args.get("show_bibtex")

        return render_template("index.html", references=citation_data,
                            references_bibtex=bibtex_data, show_bibtex=show_bibtex)
    return redirect("/login")

@app.route("/add_reference", methods=["POST"])
def add_reference():
    if user_repo.is_user():
        reference_type = request.form["reference_type"]
        reference_id = request.form["ID"]
        author = request.form["author"]
        title = request.form["title"]
        year = request.form["year"]
        citation_repo.create_citation(reference_type, reference_id, author, title, int(year),
                                      user_repo.user_id())
    return redirect("/")

@app.route("/delete_reference/<reference_id>", methods=["POST"])
def delete_reference(reference_id):
    if user_repo.is_user():
        citation_repo.delete_citation(reference_id, user_repo.user_id())
    return redirect("/")

@app.route("/delete_references", methods=["POST"])
def delete_all_references():
    if user_repo.is_user():
        citation_repo.delete_all_citations(user_repo.user_id())

    return redirect("/")


@app.route("/download_references", methods=["POST"])
def download_references():
    if user_repo.is_user():
        citation_data = citation_repo.get_citations(user_repo.user_id())
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
    return redirect("/")

@app.route('/register', methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password_hash"]

        if user_repo.create_user(username, password):
            return redirect("/")
        return error("Registeration failed, user already exists", "register")
    return redirect("/")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password_hash"]
        if user_repo.login_user(username, password):
            return redirect("/")

        return error("Wrong username or password", "login")
    return redirect("/")

@app.route('/logout', methods=["GET"])
def logout():
    user_repo.logout()
    return redirect("/")

@app.route('/delete_user', methods=["GET"])
def delete_user():
    if user_repo.is_user():
        user_repo.delete_user(user_repo.user_id())
        return redirect("/logout")
    return redirect("/")

@app.route('/get_doi', methods=["GET"])
def doi():
    if user_repo.is_user():
        doi_input = request.args.get('doiInput')
        data = bibtex_service.get_bibtex_data_from_doi(doi_input)
        if data:
            citation_repo.create_citation(data['type'], data['key'], data['author'], data['title'], data['year'],
                                          user_repo.user_id())
    return redirect ("/")
