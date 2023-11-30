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
        pl.Path(f"./{self.file_name}")
        self.cleanup()