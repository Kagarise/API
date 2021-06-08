import redis

from config import redis_config

pool = redis.ConnectionPool(**redis_config)
redis_client = redis.Redis(connection_pool=pool)
