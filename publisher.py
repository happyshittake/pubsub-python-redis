import ntpath
import sys

import redis

# cara mempublish file: python publisher.py [judul berita] [file berita]
# contoh: python publisher.py 'judul berita' berita.txt

r = redis.StrictRedis(host="localhost", port="6379", db=0)  # membuat koneksi ke redis


# fungsi untuk mempublish event ke redis server
def publish(redis_instance, t):
    redis_instance.publish("news_channel", t)


# fungsi untuk mendapat kan nama file dari path file
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


# title pada argumen no 1
title = sys.argv[1]

# dapatkan argumen no 2
filepath = sys.argv[2]

r.set("news", title)  # save judul file ke redis

f = open(filepath, 'rb').read()  # baca isi dari file

r.set('file', f)  # simpan isi file ke redis

publish(r, title)
