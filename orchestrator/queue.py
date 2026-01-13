import redis
from rq import Queue

redis_conn = redis.Redis(host="redis", port=6379)
queue = Queue("pyorch", connection=redis_conn)
