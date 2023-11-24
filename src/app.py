from enum import Enum
from services.bibtex_service import BibTextService


class ReferenceOption(Enum):
    TITLE = 1
    AUTHOR = 2
    YEAR = 3
    REFERENCE_TYPE = 4

class BibtexUi:
    def __init__(self, io):
        self._io = io
        self._run = True
        self.service = BibTextService()

    def start(self):
        while self._run:

            message = "Type the number for your action:\n1: add reference\n2: list references \n3: exit\n"
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
                        self.list_references_by()
                        continue

                    parameter = self._io.read(f"Type the {ReferenceOption(input_type).name.lower()}:\n")
                    self.list_references_by(parameter, ReferenceOption(input_type).name.lower())

                except ValueError:
                    message = "Invalid input. Please enter a correct number."
                    self._io.write(message)

            elif user_input == "3":
                self._run = False

            else:
                self._io.write("Invalid input.")

    def add_reference(self, reference_type):
        key = self._io.read("Insert reference key (viiteavain): ")
        author = self._io.read("Insert author: ")
        title = self._io.read("Insert title: ")
        year = int(self._io.read("Insert year: "))

        self._io.write(f"Added an {reference_type} {key}, titled {title} ({year}), by {author}")
        self.service.write_to_bib_file(reference_type, key, author, title, year)

    def list_references_by(self, search_term=None, content_type=None):
        bibtexdatafile = self.service.read_from_bib_file()
        if bibtexdatafile == FileNotFoundError:
            message = "Something went wrong. Probably your .bib file is empty/doesn't exist."
            self._io.write(message)
            return

        self._io.write("\nFound:\n")

        for reference in bibtexdatafile.entries:
            if not content_type or (content_type in reference and search_term in reference[content_type]):
                self._io.write(f"\nID: {reference['ID']}\n"
                f"Title: {reference['title']}\n"
                f"Author: {reference['author']}\n"
                f"Year: {reference['year']}\n"
                f"Reference type: {reference['ENTRYTYPE']}\n")
