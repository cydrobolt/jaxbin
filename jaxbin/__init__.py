from flask import Flask, render_template, request, abort
from models import *
from util import generate_token

app = Flask('jaxbin')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_bin", methods=['GET', 'POST'])
def create_bin():
    bin_data = request.form["binData"]
    bin_id = generate_token(6)

    Bin.create(
        p_id = bin_id,
        content = bin_data
    )

    if not bin_data:
        abort(400, "Invalid Request")

    return bin_id

@app.route("/<bin_id>")
def show_bin(bin_id):
    bin_obj = Bin.select().where(Bin.p_id == bin_id).first()
    return render_template("show_paste.html", paste=bin_obj)

# Open & close db connections
@app.before_request
def _db_connect():
    db.connect()

@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()
