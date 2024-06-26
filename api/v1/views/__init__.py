#!/usr/bin/python3
from flask import Blueprint
"""
Moudle to create Blueprint for our API
"""


app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")


from .states import *
from .index import *
from .cities import *
from .amenities import *
from .users import *
from .places import *
from .places_reviews import *
