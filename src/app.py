import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from entities.reference import Reference


class BibtexUi:
    def __init__(self, io):
        self._io = io
        self._run = True

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
                try:
                    bibtexdatafile = self.read_from_bib_file()
                    for reference in bibtexdatafile.entries:
                        self._io.write(reference)
                except FileNotFoundError:
                    message = "Something went wrong. Probably your .bib file is empty/doesn't exist."
                    self._io.write(message)
            elif user_input == "3":
                self._run = False

            else:
                self._io.write("Virheellinen syöte.")

    def add_reference(self, reference_type):
        key = self._io.read("Insert reference key (viiteavain): ")
        author = self._io.read("Insert author: ")
        title = self._io.read("Insert title: ")
        year = int(self._io.read("Insert year: "))

        self._io.write(f"Added an {reference_type} {key}, titled {title} ({year}), by {author}")
        output_refrence  = Reference(reference_type, key, author, title, year )
        self.write_to_bib_file(output_refrence)

    def write_to_bib_file(self, data):
        writer = BibTexWriter()
        entry = data.create_bibtex_format()
        with open("references.bib", "a", encoding="utf-8") as bibfile:
            bibfile.write(writer.write(entry))

    def read_from_bib_file(self):
        with open('references.bib', encoding="utf-8") as bibtex_file:
            bibtexdatafile = bibtexparser.load(bibtex_file)
        return bibtexdatafile
