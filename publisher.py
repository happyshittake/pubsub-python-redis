import ntpath
import os

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


def prompt_upload():
    # title pada argumen no 1
    title = input("masukkan judul file: ")

    if title is None:
        print("penggunaan: python publisher.py [judul file] [file yang akan diupload]")
        exit(1)

    # dapatkan argumen no 2
    filepath = input("masukkan file yang akan diupload: ")

    if filepath is None:
        print("harus ada file yang akan diupload")
        exit(1)

    dir_path = os.path.dirname(os.path.realpath(__file__))

    r.set("news", title)  # save judul file ke redis

    f = open(dir_path + "/" + filepath, 'rb').read()  # baca isi dari file

    r.set('file', f)  # simpan isi file ke redis

    publish(r, title)

    print("file berhasil di upload")


prompt_upload()

re = input("apakah anda mau upload lagi? y/n - ")

while re is not 'n':
    prompt_upload()
