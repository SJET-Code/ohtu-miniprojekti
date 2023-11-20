import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from entities.reference import Reference

class BibTextService:
    def __init__(self):
        pass

    def write_to_bib_file(reference_type, key, author, title, year):
        reference  = Reference(reference_type, key, author, title, year)
        writer = BibTexWriter()
        entry = reference.create_bibtex_format()
        with open("references.bib", "a", encoding="utf-8") as bibfile:
            bibfile.write(writer.write(entry))

    def read_from_bib_file():
        with open('references.bib', encoding="utf-8") as bibtex_file:
            bibtexdatafile = bibtexparser.load(bibtex_file)
        return bibtexdatafile