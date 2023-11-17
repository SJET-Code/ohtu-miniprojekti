import unittest
from entities.reference import Reference

class TestReference(unittest.TestCase):
    def setUp(self):
        self.reference = Reference("article", "abcdef", "aaa", "bbb", 2023)

    def test_creates_bibtex_format_correctly(self):
        model_entry = {
            "title": 'bbb',
            "author": "aaa",
            "year": "2023",
            "ENTRYTYPE": "article",
            "ID": "abcdef"
        }

        bibtex = self.reference.create_bibtex_format()
        entry = bibtex.entries[0]

        self.assertEqual(entry, model_entry)
