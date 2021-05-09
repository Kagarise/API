from flask import Blueprint, request

from ..models import *

api = Blueprint('api_v1', __name__)


@api.route('/hand_painting', methods=['post'])
def hand_painting():
    url = request.json.get('url')
    return get_hand_painting(url=url)
