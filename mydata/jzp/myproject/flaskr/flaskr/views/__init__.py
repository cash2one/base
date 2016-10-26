from flask import Blueprint

instance = Blueprint('instance', __name__, template_folder="templates")

from . import flaskr


