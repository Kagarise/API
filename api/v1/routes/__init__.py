from flask import Blueprint, request

from utils.response import Res
from ..models import *
from ..models.rontgen import get_rontgen_data

api = Blueprint('api_v1', __name__)


@api.route('/hand_painting', methods=['post'])
def hand_painting():
    url = request.json.get('url')
    if url is None:
        return Res.error(400, 'Args error!')
    url = get_hand_painting(url=url)
    if url is None:
        return Res.error(500, "url为None")
    else:
        data = {
            'url': url
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
            return Res.error(500, 'url为None')
        else:
            data = {
                'url': url
            }
            return Res.success(data=data)
    except:
        return Res.error(403, "请求aip错误")


@api.route('/yourls', methods=['post'])
def yourls():
    url = request.json.get('url')
    if url is None:
        return Res.error(400, 'Args error!')
    url = get_yourls(url=url)
    if url is None:
        return Res.error(500, "url为None")
    else:
        data = {
            'url': url
        }
        return Res.success(data=data)


@api.route('/qr', methods=['post'])
def qr():
    tex = request.json.get('tex')
    if tex is None:
        return Res.error(400, 'Args error!')
    url = get_qr(tex=tex)
    if url is None:
        return Res.error(500, "url为None")
    else:
        data = {
            'url': url
        }
        return Res.success(data=data)


@api.route('/rontgen_code', methods=['post'])
def rontgen_code():
    tex = request.json.get('tex')
    if tex is None:
        return Res.error(400, 'Args error!')
    num = request.json.get('num')
    if num is None:
        num = 1
    else:
        try:
            if int(num) <= 0:
                return Res.error(400, 'num必须大于0')
        except:
            return Res.error(400, 'num必须为整数')
    typ = request.json.get('typ')
    if typ is None:
        typ = 'forever'
    elif typ not in ['times', 'minute', 'hour', 'day', 'forever']:
        return Res.error(400, 'typ不合规范')
    pwd = request.json.get('pwd')
    url = get_rontgen_code(tex=tex, num=num, typ=typ, pwd=pwd)
    if url is None:
        return Res.error(500, "url为None")
    else:
        data = {
            'url': url
        }
        return Res.success(data=data)


@api.route('/rontgen_data', methods=['post'])
def rontgen_data():
    id = request.json.get('id')
    if id is None:
        return Res.error(400, 'Args error!')
    data = get_rontgen_data(id=id)
    if data is None:
        return Res.error(500, "data为None")
    else:
        return Res.success(data=data)
