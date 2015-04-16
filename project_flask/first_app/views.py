from flask import render_template

from ..first_app import first_app


@first_app.route('/', methods=['GET', ])
def index():
    return render_template('index.html')
