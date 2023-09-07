import json

from helpers.redis_handler import RedisCache
from pipes.banxico_api.banxico_client import Banxico

cache = RedisCache(ttl=5 * 60)


@cache.cache
def save_banxico_data(data):
    return data


def get_banxico_data() -> bool:
    api = Banxico()
    data = api.banxico_get_series_datos("SF43718")
    if data.status_code == 200:
        return json.loads(data.text)
    return False
