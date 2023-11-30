import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from entities.reference import Reference
from services.file_service import FileService

class BibTextService:
    def __init__(self):
        self._file_service = FileService()

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

    def rewrite_bib_file(self, references, file_name = None):
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
        if file_name is None:
            self._file_service.create_file_if_not_exists("references.bib")
        else:
            self._file_service.create_file_if_not_exists(file_name + ".bib")

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

    def delete_from_bib_file(self, reference_id, references, file_name = None):
        copyreferencelist = []

        for value in references.entries:
            if value.get("ID") != reference_id:
                copyreferencelist.append(value)

        bibtex_reference_list = self._reference_list_generator(copyreferencelist)
        self.rewrite_bib_file(bibtex_reference_list, file_name)

    def delete_all_from_bib_file(self, file_name = None):
        self.rewrite_bib_file([], file_name)

    def _reference_list_generator(self, references):
        new_references_list = []
        #can/should be expanded for each specific entrytype
        for reference in references:
            new_reference = Reference(reference["ENTRYTYPE"], reference["ID"],
                reference["author"], reference["title"], reference["year"],)
            new_references_list.append(new_reference)
        return new_references_list
