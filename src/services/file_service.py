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
            with open(filename, "x", encoding="utf-8") as new_file:
                return f"{new_file} created succesfully.\n"
        except FileExistsError:
            return f"{filename} is already existent.\n"
