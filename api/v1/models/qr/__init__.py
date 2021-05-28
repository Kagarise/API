import os
from time import time

import qrcode

from utils.cos import cos_config, upload_local_file
from utils.logger import logger


def get_qr(tex):
    qr = qrcode.QRCode(border=2)
    qr.add_data(tex)
    qr.make(fit=True)
    img = qr.make_image()
    file_path = f'source/qr/{int(time())}.jpg'
    img.save(file_path)
    upload_local_file(bucket_name=cos_config['BucketName'], local_file_path=file_path, file_path=file_path)
    if os.path.exists(file_path):
        os.remove(file_path)
    qr_url = f'{cos_config["Prefix"]}{file_path}'
    logger.success(f"{tex}已被处理成qr码")
    return qr_url
