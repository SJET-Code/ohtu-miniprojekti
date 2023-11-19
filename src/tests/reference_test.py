import unittest
from entities.reference import Reference
from app import BibtexUi
from unittest.mock import Mock

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

    def test_add_new_reference_returns_correct_output(self):
        mock_io = Mock()
        bibtext_ui = BibtexUi(mock_io)

        mock_io.read.side_effect = ['key1', 'aaa', 'title1', '2022']
        bibtext_ui.add_reference("book")

        expected_output = "Added an book key1, titled title1 (2022), by aaa"
        mock_io.write.assert_called_once_with(expected_output)