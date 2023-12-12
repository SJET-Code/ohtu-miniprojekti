"""initilizes application"""
from flask import Flask
from config import SECRET_KEY
from services.error_handler import ErrorHandler
from services.validation_service import ValidationError

app = Flask(__name__)
app.secret_key = SECRET_KEY

error_handler = ErrorHandler()
app.register_error_handler(ValidationError, error_handler.handle_validation_error)
app.register_error_handler(Exception, error_handler.handle_standard_error)

import routes # pylint: disable=W0611
