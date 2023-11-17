from app import BibtexUi
from reader_writer import ReaderWriter

def main():
    io = ReaderWriter()
    ui = BibtexUi(io)
    ui.start()


if __name__ == "__main__":
    main()
