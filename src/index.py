from app import BibtexUi
from services.io_service import IOService

def main():
    io = IOService()
    ui = BibtexUi(io)
    ui.start()


if __name__ == "__main__":
    main()
