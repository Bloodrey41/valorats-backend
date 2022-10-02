from flask import Blueprint, jsonify
from .data import data

bp = Blueprint('api', __name__, url_prefix = '/api')

@bp.route('/', methods = ['GET'])
def index():
    return jsonify(data)
