"""initilizes application"""
from flask import Flask
from config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

import routes # pylint: disable=W0611
