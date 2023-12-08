import unittest
from services.bibtex_service import BibTextService
from services.file_service import FileService

class TestBibTextService(unittest.TestCase):
    def setUp(self):
        self.file_name = "test_references"

        file_service = FileService()
        file_service.create_file_if_not_exists(self.file_name + ".bib")

        self.bibtex_service = BibTextService()
        self.bibtex_service.rewrite_bib_file([], self.file_name)
        self.bibtex_service.write_to_bib_file("article", "abcdef", "aaa", "bbb", 2023, self.file_name)

    def test_reads_from_bibtex_file_correctly(self):
        model_entry = {
            "title": 'bbb',
            "author": "aaa",
            "year": "2023",
            "ENTRYTYPE": "article",
            "ID": "abcdef"
        }

        bibtex_data = self.bibtex_service.read_from_bib_file(self.file_name)
        entry = bibtex_data.entries[0]

        self.assertDictEqual(entry, model_entry)

    def test_writes_into_bibtex_file_correctly(self):
        model_string = ("@article{abc,\n"+
                        " author = {def},\n"+
                        " title = {ghi},\n"+
                        " year = {2013}\n}")

        self.bibtex_service.write_to_bib_file("article", "abc", "def", "ghi", 2013, self.file_name)

        with open(self.file_name + ".bib", "r", encoding="utf-8") as bibtex_file:
            file_content = bibtex_file.read()

        self.assertTrue(model_string in file_content)

    def test_writes_into_new_bibfile_if_filename_is_none(self):
        model_string = ("@article{abc,\n"+
                        " author = {def},\n"+
                        " title = {ghi},\n"+
                        " year = {2013}\n}")

        self.bibtex_service.write_to_bib_file("article", "abc", "def", "ghi", 2013)

        with open("references.bib", "r", encoding="utf-8") as bibtex_file:
            file_content = bibtex_file.read()

        self.assertTrue(model_string in file_content)

    def test_deletes_from_bibtex_file_correctly(self):
        self.bibtex_service.delete_all_from_bib_file(self.file_name)

        bibtex_data = self.bibtex_service.read_from_bib_file(self.file_name)

        self.assertEqual(bibtex_data.entries, [])

    def test_deleting_all_deletes_multiple_references(self):
        self.bibtex_service.write_to_bib_file("article", "abc", "def", "ghi", 2013, self.file_name)

        self.bibtex_service.rewrite_bib_file([], self.file_name)

        bibtex_data = self.bibtex_service.read_from_bib_file(self.file_name)

        self.assertEqual(bibtex_data.entries, [])

    def test_deleting_one_reference_does_not_delete_others(self):
        model_entry = {
            "title": "ghi",
            "author": "def",
            "year": "2013",
            "ENTRYTYPE": "article",
            "ID": "abc"
        }

        self.bibtex_service.write_to_bib_file("article", "abc", "def", "ghi", 2013, self.file_name)
        bibtex_data = self.bibtex_service.read_from_bib_file(self.file_name)

        self.bibtex_service.delete_from_bib_file("abcdef", bibtex_data, self.file_name)

        bibtex_data = self.bibtex_service.read_from_bib_file(self.file_name)

        self.assertDictEqual(bibtex_data.entries[0], model_entry)

    def test_adding_reference_with_correct_doi(self):
        model_entry = {
            "title": "Gold‐Catalyzed Cycloisomerization of Sulfur Ylides to Dihydrobenzothiepines",
            "author": "Knittl‐Frank, Christian and Saridakis, Iakovos and Stephens, Thomas and Gomes, Rafael and Neuhaus, James and Misale, Antonio and Oost, Rik and Oppedisano, Alberto and Maulide, Nuno",
            "year": "2020",
            "ENTRYTYPE": "article",
            "ID": "Knittl_Frank_2020"
        }

        doi = "10.1002/chem.202000622"

        data = self.bibtex_service.get_bibtex_data_from_doi(doi)

        self.bibtex_service.write_to_bib_file(data['type'], data['key'], data['author'], data['title'], data['year'], self.file_name)

        bibtex_data = self.bibtex_service.read_from_bib_file(self.file_name)

        self.assertDictEqual(bibtex_data.entries[1], model_entry)

    def test_adding_reference_with_incorrect_doi(self):
        doi = "invalid-doi"
        self.assertIsNone(self.bibtex_service.get_bibtex_data_from_doi(doi))

        bibtex_data = self.bibtex_service.read_from_bib_file(self.file_name)

        self.assertEqual(len(bibtex_data.entries), 1)

