#!/usr/bin/python3
"""Init"""
# Wildcard import to avoid circular import errors
from api.v1.views import *

from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
