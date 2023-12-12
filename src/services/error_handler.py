from flask import flash, redirect

class ErrorHandler:
    def __init__(self) -> None:
        self.error_messages = []

    def handle_validation_error(self, error):
        flash(str(error))

        return redirect(error.route_to)

    def handle_standard_error(self, error): # pylint: disable=W0613
        return redirect("/")
