import redis

r = redis.StrictRedis(host="localhost", port="6379", db=0)


def displaymesages():
    coll = r.lrange("news", 0, -1)
    idx = 1
    for n in coll:
        print("%d %s" % (idx, n.decode('utf-8')))
        idx += 1


displaymesages()
pubsub = r.pubsub()

try:
    pubsub.subscribe(["news_channel"])
    while True:
        for message in pubsub.listen():
            if message['data'] != 1:
                print("berita baru: %s" % message['data'].decode('utf-8'))
                displaymesages()
except KeyboardInterrupt:
    pubsub.close()
    print("exiting")
