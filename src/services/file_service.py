from os import remove

class FileService:
    def __init__(self):
        pass

    def remove_bibtex_file(self, filename):
        try:
            remove(filename)
            return f"{filename} removed succesfully.\n"
        except FileNotFoundError:
            return "File not found\n"

    def add_bibtex_file(self, filename):
        try:
            with open(filename, "x", encoding="utf-8"):
                return f"{filename} created succesfully.\n"
        except FileExistsError:
            return f"{filename} is already existent.\n"

    def create_file_if_not_exists(self, filename):
        try:
            with open(filename, "x", encoding="utf-8"):
                pass
        except FileExistsError:
            pass
