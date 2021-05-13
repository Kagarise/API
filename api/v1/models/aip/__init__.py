import os
from time import time

import requests

from utils.cos import cos_config, upload_local_file
from utils.logger import logger

access_token_api = 'https://openapi.baidu.com/oauth/2.0/token'
aip_api = 'http://tsn.baidu.com/text2audio'


def get_access_token(client_id, client_secret):
    params = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    token_result = eval(requests.post(access_token_api, params=params).text)
    return token_result


# https://ai.baidu.com/ai-doc/SPEECH/Qk38y8lrl
def get_aip(API_KEY, SECRET_KEY, tex, cuid='kagarise', ctp=1, lan='zh', spd=5, pit=5, vol=5, per=103, aue=3):
    tok = get_access_token(client_id=API_KEY, client_secret=SECRET_KEY)
    try:
        access_token = tok['refresh_token']
        logger.success(f'获取token成功')
    except:
        access_token = None
        logger.error(f'获取token失败')
    print(access_token)
    params = {
        'tex': tex,
        'tok': access_token,
        'cuid': cuid,
        'ctp': ctp,
        'lan': lan,
        'spd': spd,
        'pit': pit,
        'vol': vol,
        'per': per,
        'aue': aue
    }
    result = requests.post(aip_api, params=params)
    if not isinstance(result, dict):
        file_path = f'source/aip/{int(time())}.mp3'
        with open(file_path, 'wb') as f:
            f.write(result.content)
        upload_local_file(bucket_name=cos_config['BucketName'], local_file_path=file_path, file_path=file_path)
        if os.path.exists(file_path):
            os.remove(file_path)
        logger.success("请求aip成功")
        return f'{cos_config["Prefix"]}{file_path}'
    else:
        logger.error("请求aip失败")
        return None
