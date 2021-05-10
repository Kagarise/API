from flask import Blueprint, request

from utils.response import Res
from ..models import *

api = Blueprint('api_v1', __name__)


@api.route('/hand_painting', methods=['post'])
def hand_painting():
    url = request.json.get('url')
    data = {
        'url': get_hand_painting(url=url)
    }
    return Res.success(data=data)
