import hashlib
import time
import requests

from utils.logger import logger


def get_yourls(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        url = "http://" + url
    api = "http://yourls.flora.love/yourls-api.php"
    timestamp = str(int(time.time()))
    signature = "755abd5c4d"
    signature = hashlib.md5((timestamp + signature).encode('utf8')).hexdigest()
    action = "shorturl"
    format = "json"
    params = {
        'timestamp': timestamp,
        'signature': signature,
        'action': action,
        'format': format,
        'url': url
    }
    try:
        data = eval(requests.get(api, params=params).text)
        logger.success(f'{url}被处理为{data["shorturl"]}')
        return data
    except:
        logger.error(f"短链接请求错误：{url}")
        return None
# {
# 	"code": 200,
# 	"msg": "",
# 	"data": {
# 		"url": {
# 			"url": {
# 				"keyword": "d2uS",
# 				"url": "https:\\/\\/www.baidu.com",
# 				"title": "https:\\/\\/www.baidu.com",
# 				"date": "2021-05-28 09:33:13",
# 				"ip": "125.47.41.156"
# 			},
# 			"status": "success",
# 			"message": "https:\\/\\/www.baidu.com 已保存为",
# 			"title": "https:\\/\\/www.baidu.com",
# 			"shorturl": "http:\\/\\/yourls.flora.love\\/d2uS",
# 			"statusCode": 200
# 		}
# 	}
# }
# {
# 	"code": 200,
# 	"msg": "",
# 	"data": {
# 		"url": {
# 			"status": "fail",
# 			"code": "error:url",
# 			"url": {
# 				"keyword": "d2uS",
# 				"url": "https:\\/\\/www.baidu.com",
# 				"title": "https:\\/\\/www.baidu.com",
# 				"date": "2021-05-28 09:33:13",
# 				"ip": "125.47.41.156",
# 				"clicks": "0"
# 			},
# 			"message": "https:\\/\\/www.baidu.com 已经存在",
# 			"title": "https:\\/\\/www.baidu.com",
# 			"shorturl": "http:\\/\\/yourls.flora.love\\/d2uS",
# 			"statusCode": 200
# 		}
# 	}
# }
