"""Directs user to different parts of the website"""
from flask import redirect, render_template, request
from flask_app import app
from services.bibtex_service import BibTextService
from repositories.citation_repository import CitationRepository
from database import db

citation_repo = CitationRepository(db)
bibtex_service = BibTextService()

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
    try:
        bibtex_service.delete_all_from_bib_file()
        citation_repo.delete_all_citations()
    except Exception as e:
        print(f"Error deleting references: {e}")
        

    return redirect("/")
