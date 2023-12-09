"""initilizes application"""
from flask import Flask
from config import SECRET_KEY

app = Flask(__name__, static_folder='build', static_url_path='')
app.secret_key = SECRET_KEY

import routes # pylint: disable=W0611
