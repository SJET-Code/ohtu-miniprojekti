from flask import Flask, render_template, request, redirect
from app import BibtexUi
from services.io_service import IOService
from services.bibtex_service import BibTextService

app = Flask(__name__)
io = IOService()
ui = BibtexUi(io)

bibtex_service = BibTextService()

@app.route("/")
def index():
    bibtexdatafile = bibtex_service.read_from_bib_file()

    return render_template("index.html", references=bibtexdatafile.entries)

@app.route("/add_reference", methods=["POST"])
def add_reference():
    reference_type = request.form["reference_type"]
    reference_id = request.form["ID"]
    author = request.form["author"]
    title = request.form["title"]
    year = request.form["year"]

    bibtex_service.write_to_bib_file(reference_type, reference_id, author, title, year)

    return redirect("/")

@app.route("/delete_reference/<reference_id>", methods=["POST"])
def delete_reference(reference_id):
    bibtex_data = bibtex_service.read_from_bib_file()
    bibtex_service.delete_from_bib_file(reference_id, bibtex_data)

    return redirect("/")

@app.route("/delete_references", methods=["POST"])
def delete_all_references():
    bibtex_service.delete_all_from_bib_file()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
