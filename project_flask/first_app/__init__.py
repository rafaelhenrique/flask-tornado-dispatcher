from flask import Blueprint

first_app = Blueprint('first_app', __name__, template_folder='templates')

from ..first_app import views
