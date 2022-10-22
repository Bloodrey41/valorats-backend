from flask import Blueprint, jsonify, request
from .data import get_data
import requests

bp = Blueprint('api', __name__, url_prefix = '/api')

@bp.route('/', methods = ['GET'])
def index():
    url = request.args.get('url')
    data = get_data(url)
    return jsonify(data)
