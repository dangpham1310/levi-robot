from flask import Blueprint

routes = Blueprint('routes', __name__)
from .login import *
from .users import*
from .register import *
from .dashboard import*