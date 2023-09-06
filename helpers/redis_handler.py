import redis


class RedisCache:
    def __init__(self, host="localhost", port=6379, ttl=3600):
        self.client = redis.StrictRedis(host=host, port=port, decode_responses=True)
        self.ttl = ttl  # Time-to-live in seconds

    def set(self, key, value):
        self.client.setex(key, self.ttl, value)

    def get(self, key):
        return self.client.get(key)

    def delete(self, key):
        self.client.delete(key)

    def cache(self, func):
        """Decorator to cache function results using Redis."""

        def wrapper(*args, **kwargs):
            cache_key = f"{func.__name__}:{args}:{kwargs}"
            cached_value = self.get(cache_key)
            if cached_value:
                print("Cache hit!")
                return cached_value
            result = func(*args, **kwargs)
            self.set(cache_key, result)
            return result

        return wrapper
