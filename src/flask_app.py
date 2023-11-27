from flask import Flask, render_template, request
from app import BibtexUi
from services.io_service import IOService

app = Flask(__name__)
io = IOService()
ui = BibtexUi(io)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_reference", methods=["POST"])
def add_reference():
    reference_type = request.form["reference_type"] # pylint: disable=W0612
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
