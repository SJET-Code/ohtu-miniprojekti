from bibtexparser.bibdatabase import BibDatabase

class Reference:
    def __init__(self, reference_type, key, author, title, year):
        self._type = reference_type
        # Referring to the \cite{VPL11} (VPL11) value in the latex, for example.
        self._key = key
        self._author = author
        self._title = title
        self._year = year

    def create_bibtex_format(self):
        bibtex_format = BibDatabase()
        bibtex_format.entries = [
            {
                "title": self._title,
                "author": self._author,
                "year": str(self._year),
                 "ENTRYTYPE": self._type,
                 "ID": self._key
            }
        ]

        return bibtex_format
    
    
