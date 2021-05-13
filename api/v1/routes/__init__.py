from flask import Blueprint, request

from utils.response import Res
from ..models import *

api = Blueprint('api_v1', __name__)


@api.route('/hand_painting', methods=['post'])
def hand_painting():
    url = request.json.get('url')
    if url is None:
        return Res.error(400, 'Args error!')
    data = {
        'url': get_hand_painting(url=url)
    }
    return Res.success(data=data)


@api.route('/aip', methods=['post'])
def hand_aip():
    API_KEY = request.json.get('API_KEY')
    SECRET_KEY = request.json.get('SECRET_KEY')
    if API_KEY is None or SECRET_KEY is None:
        return Res.forbidden()
    tex = request.json.get('tex')
    if tex is None:
        return Res.error(400, 'Args error!')
    per = request.json.get('per')
    if per is None:
        per = 5118
    try:
        url = get_aip(API_KEY=API_KEY, SECRET_KEY=SECRET_KEY, tex=tex, per=per)
        if url is None:
            return Res.error(403, 'url为None')
        else:
            data = {
                'url': url
            }
            return Res.success(data=data)
    except:
        return Res.error(403, "请求aip错误")
