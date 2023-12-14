import bibtexparser
import requests
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bparser import BibTexParser
from entities.reference import Reference
from services.file_service import FileService

class BibTextService:
    def __init__(self):
        self._file_service = FileService()

    def write_to_bib_file(self,reference_type, key, author, title, year, file_name = None):
        reference = Reference(reference_type, key, author, title, year)
        bibtex = self.get_bibtex_string(reference)

        if not file_name:
            with open("references.bib", "a", encoding="utf-8") as bibfile:
                bibfile.write(bibtex)
        else:
            with open(f"{file_name}.bib", "a", encoding="utf-8") as bibfile:
                bibfile.write(bibtex)

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
        copyreferencelist = [value for value in references.entries if value.get("ID") != reference_id]

        bibtex_reference_list = self._reference_list_generator(copyreferencelist)
        self.rewrite_bib_file(bibtex_reference_list, file_name)

    def delete_all_from_bib_file(self, file_name = None):
        self.rewrite_bib_file([], file_name)

    def get_bibtex_string(self, reference):
        writer = BibTexWriter()
        entry = reference.create_bibtex_format()

        return writer.write(entry)

    def get_references_in_bibtex_format(self, references):
        references_bibtex = []

        for reference in references:
            references_bibtex.append(self.get_bibtex_string(reference))

        return references_bibtex

    def _reference_list_generator(self, references):
        new_references_list = []

        for reference in references:
            new_reference = Reference(reference["ENTRYTYPE"], reference["ID"],
                reference["author"], reference["title"], reference["year"],)
            new_references_list.append(new_reference)
        return new_references_list

    def _parse_doi_data(self, entry):
        entrytype = entry.get('ENTRYTYPE', '')
        key = entry.get('ID', '')
        author = entry.get('author', '')
        title = entry.get('title', '')
        year = entry.get('year', '')
        return {
            "type": entrytype,
            "key": key,
            "author": author,
            "title": title,
            "year": year
        }

    def _doi_request(self, doi_input):
        if not doi_input:
            return None
        url =  "http://dx.doi.org/" + doi_input
        headers = {"accept": "application/x-bibtex"}
        timeout_seconds = 5
        request = requests.get(url, headers=headers, timeout=timeout_seconds)
        if request.status_code == 200:
            bib_data = request.text
            parser = BibTexParser()
            bib_database = bibtexparser.loads(bib_data, parser=parser)
            entry = bib_database.entries[0]
            return self._parse_doi_data(entry)
        return None

    def get_bibtex_data_from_doi(self, doi_input):
        parsed_data = self._doi_request(doi_input)
        if parsed_data:
            return parsed_data
        return None
