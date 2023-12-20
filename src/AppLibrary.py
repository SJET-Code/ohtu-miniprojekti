# pylint: disable=C0103
from app import BibtexUi
from services.io_service import StubIOService
from routes import citation_repo

class AppLibrary:
    def __init__(self):
        self._io = StubIOService()
        self.stub_ui = BibtexUi(self._io, True)
        self.citation_repo = citation_repo

    def start(self):
        self.stub_ui.start()

    def input(self, value):
        self._io.add_input(value)

    def output_should_contain(self, value):
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def output_should_not_contain(self, value):
        outputs = self._io.outputs

        if value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is in {str(outputs)}"
            )

    def reset_outputs(self):
        self._io.reset_outputs()

    def reset_bibtexfile(self):
        self.stub_ui.remove_reference("DELALL")
