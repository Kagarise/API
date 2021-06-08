from time import time

from utils.id import create_id
from utils.pedis import redis_client
from utils.logger import logger


def id_is_exist(id):
    return redis_client.exists(id)


# key: id
# value: {
#   tex: string,
#   typ: string(once, hour, forever),
#   create_time, timestamp(int),
#   use_times: int,
# }

def get_rontgen_code(tex, typ):
    id_length = 6
    id = create_id(id_length)
    try:
        while id_is_exist(id):
            id = create_id(id_length)
    except:
        return None
    logger.success(f"生成id<{id}>")
    data = {
        'tex': tex,
        'typ': typ,
        'create_time': int(time()),
        'use_times': 0
    }
    try:
        redis_client.hset(id, mapping=data)
        logger.success(f"<{id}>存放数据成功")
        return id
    except:
        return None


def data_is_disable(id, data):
    new_data = data.copy()
    new_data['use_times'] = int(new_data['use_times']) + 1
    try:
        redis_client.hset(id, mapping=new_data)
    except:
        return True
    logger.success(f"<{id}>更新数据成功")
    if data['typ'] == 'once' and int(data['use_times']) > 0:
        return True
    elif data['typ'] == 'hour' and int(time()) - int(data['create_time']) > 3600:
        return True
    else:
        return False


def get_rontgen_data(id):
    if not id_is_exist(id):
        return None
    try:
        data = redis_client.hgetall(id)
        logger.success(f"<{id}>取出数据成功")
        if data_is_disable(id, data):
            logger.warning(f"<{id}>数据不可用")
            return None
        return data
    except:
        return None


if __name__ == "__main__":
    id = get_rontgen_code("你好", "once")
    print(get_rontgen_data(id))
