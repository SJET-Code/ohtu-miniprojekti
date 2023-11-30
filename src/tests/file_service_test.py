import unittest
from services.file_service import FileService
import pathlib as pl

class TestFileService(unittest.TestCase):
    def setUp(self):
        self.file_name = "test_references_file.bib"

        self.file_service = FileService()

    def cleanup(self):
        self.file_service.remove_bibtex_file(self.file_name)

    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))
        
    def test_bibfile_can_be_created(self):
        self.file_service.add_bibtex_file(self.file_name)
        self.assertIsFile(f"./{self.file_name}")

    def test_bibfile_error_if_exists(self):
        self.file_service.add_bibtex_file(self.file_name)
        fail = self.file_service.add_bibtex_file(self.file_name)
        self.assertAlmostEqual(fail, f"{self.file_name} is already existent.\n")

    def test_file_deteled_succesfully(self):
        self.file_service.add_bibtex_file(self.file_name)
        success = self.file_service.remove_bibtex_file(self.file_name)
        self.assertAlmostEqual(success, f"{self.file_name} removed succesfully.\n")

    def test_non_existent_file_delete(self):
        fail = self.file_service.remove_bibtex_file(self.file_name)
        self.assertAlmostEqual(fail, "File not found\n")
