import json


class Res:
    @staticmethod
    def success(data, msg=""):
        return json.dumps({
            'code': 200,
            'msg': msg,
            'data': data
        }, ensure_ascii=False)

    @staticmethod
    def error(code=400, msg=""):
        return json.dumps({
            'code': code,
            'msg': msg,
        }, ensure_ascii=False)

    @staticmethod
    def forbidden():
        return json.dumps({
            'code': 401,
            'msg': "需要认证"
        })
