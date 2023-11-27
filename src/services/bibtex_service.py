import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from entities.reference import Reference

class BibTextService:
    def __init__(self):
        pass

    def write_to_bib_file(self,reference_type, key, author, title, year, file_name = None):
        reference  = Reference(reference_type, key, author, title, year)
        writer = BibTexWriter()
        entry = reference.create_bibtex_format()
        if not file_name:
            with open("references.bib", "a", encoding="utf-8") as bibfile:
                bibfile.write(writer.write(entry))
        else:
            with open(f"{file_name}.bib", "a", encoding="utf-8") as bibfile:
                bibfile.write(writer.write(entry))

    #it basically rewrites the file, change name if other usages than delete exist.
    def delete_from_bib_file(self, references, file_name = None):
        writer = BibTexWriter()
        if not file_name:
            with open("references.bib", "w", encoding="utf-8") as bibfile:
                for reference in references:
                    bibfile.write(writer.write(reference.create_bibtex_format()))
        else:
            with open(f"{file_name}.bib", "w", encoding="utf-8") as bibfile:
                for reference in references:
                    bibfile.write(writer.write(reference.create_bibtex_format()))


    def read_from_bib_file(self, file_name = None):
        try:
            if not file_name:
                with open('references.bib', encoding="utf-8") as bibtex_file:
                    bibtexdatafile = bibtexparser.load(bibtex_file)
            else:
                with open(f'{file_name}.bib', encoding="utf-8") as bibtex_file:
                    bibtexdatafile = bibtexparser.load(bibtex_file)
        except FileNotFoundError:
            return FileNotFoundError
        return bibtexdatafile
