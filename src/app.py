from enum import Enum
from services.bibtex_service import BibTextService
from services.file_service import FileService

class ReferenceOption(Enum):
    TITLE = 1
    AUTHOR = 2
    YEAR = 3
    REFERENCE_TYPE = 4

class BibtexUi:
    def __init__(self, io, test = False):
        self._io = io
        self._run = True
        self.service = BibTextService()
        self._test = test

    def start(self):
        while self._run:

            message = ("Type the number for your action: "+
            "\n1: add reference\n2: list references \n3: remove reference\n4: manage bibtex file\n5: exit\n")
            user_input = self._io.read(message)

            if user_input == "1":
                message = ("Choose your reference you want to add by number:" +
                           "\n1: inproceedings\n2: article \n3: book\n4: other\n")
                choose_reference = self._io.read(message)
                if choose_reference == "1":
                    self.add_reference("inproceedings")
                elif choose_reference == "2":
                    self.add_reference("article")
                elif choose_reference == "3":
                    self.add_reference("book")

                # If choosing "other" references, input has to be a one what bittexparser
                # recognizes as one (i.e: inbook, phdthesis, misc, etc  ) to avoid errors.
                elif choose_reference == "4":
                    custom_reference_type = self._io.read(("Write your reference\n"))
                    self.add_reference(custom_reference_type)

            elif user_input == "2":
                message = ("List by:"+
                           "\n1: title\n2: author\n3: year\n4: reference type\n5: list all\n")
                try:
                    input_type = int(self._io.read(message))

                    if input_type == 5:
                        self._io.write(self.service.get_search_results())
                        continue

                    parameter = self._io.read(f"Type the {ReferenceOption(input_type).name.lower()}:\n")
                    self._io.write(self.service.get_search_results(parameter, ReferenceOption(input_type).name.lower()))

                except ValueError:
                    message = "Invalid input. Please enter a correct number."
                    self._io.write(message)

            elif user_input == "3":
                message = 'Write the ID/Key of the article you want to delete or type "DELALL" to delete all:\n'

                try:
                    self.list_references_by()
                    input_type = str(self._io.read(message))
                    self.remove_reference(input_type)
                except ValueError:
                    message = "Invalid input. Please enter a correct or existing ID!."
                    self._io.write(message)

            elif user_input == "4":
                message = ("Manage bibtex file" +
                           "\n1: create empty .bib file\n2: delete bibtex file\n")
                choose_reference = self._io.read(message)

                if choose_reference == "1":
                    message = FileService.add_bibtex_file(self, "./references.bib")

                elif choose_reference == "2":
                    message = FileService.remove_bibtex_file(self, "./references.bib")
                self._io.write(message)

            elif user_input == "5":
                self._run = False

            else:
                self._io.write("Invalid input.")

    def add_reference(self, reference_type):
        key = self._io.read("Insert reference key (viiteavain): ")
        author = self._io.read("Insert author: ")
        title = self._io.read("Insert title: ")
        year = int(self._io.read("Insert year: "))

        self._io.write(f"Added an {reference_type} {key}, titled {title} ({year}), by {author}")
        if self._test:
            self.service.write_to_bib_file(reference_type, key, author, title, year, 'test_references')
        else:
            self.service.write_to_bib_file(reference_type, key, author, title, year)

    def remove_reference(self, reference_id):
        if reference_id == "DELALL":
            if self._test:
                self.service.delete_all_from_bib_file('test_references')
            else:
                self.service.delete_all_from_bib_file()
            return
        references = self.service.read_from_bib_file()

        if self._test:
            self.service.delete_from_bib_file(reference_id, references,'test_references')
        else:
            self.service.delete_from_bib_file(reference_id, references)
