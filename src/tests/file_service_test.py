import unittest
from services.file_service import FileService
import pathlib as pl

class TestFileService(unittest.TestCase):
    def setUp(self):
        self.file_name = "test_references.bib"

        self.file_service = FileService()
        # file_service.create_file_if_not_exists(self.file_name + ".bib")

    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))
        return 1
        
    def bibfile_can_be_created(self):
        self.file_service.add_bibtex_file(self.file_name)

        path = pl.Path(f"../{self.file_name}")
        helper = self.assertIsFile(path)
        
        self.assertTrue(helper, 1)
