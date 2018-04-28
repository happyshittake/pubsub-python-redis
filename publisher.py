import sys

import redis

r = redis.StrictRedis(host="localhost", port="6379", db=0)


def publish(redis_instance, t):
    redis_instance.publish("news_channel", t)


title = sys.argv[1]

r.rpush("news", title)

publish(r, title)
