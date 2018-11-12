# third-party imports
from flask import Blueprint

warehouse = Blueprint('warehouse', __name__)

# local imports
from . import views