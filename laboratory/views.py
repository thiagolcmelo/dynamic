# third-party
from flask import render_template, url_for

# locals
from . import laboratory

@laboratory.route('/')
def index():
    return render_template("laboratory/index.html")

@laboratory.route('/lab')
@laboratory.route('/lab/<int:device_id>')
def lab(device_id=None):
    return render_template("laboratory/lab.html", page="lab")

# @laboratory.route('/device', methods=['GET', 'POST', 'PATCH', 'DELETE']):
