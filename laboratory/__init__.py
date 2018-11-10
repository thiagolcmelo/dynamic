# third-party imports
from flask import Blueprint

laboratory = Blueprint('laboratory', __name__)

# local imports
from . import views