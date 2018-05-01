import redis

r = redis.StrictRedis(host="localhost", port="6379", db=0)


# fungsi untuk mendownload file
def download_file(t):
    file = r.get('file')
    f = open("%s-client.txt" % t.decode('utf-8'), 'wb')
    f.write(file)
    f.close()
    print("file berhasi didownload")


title = r.get("news")  # dapatkan judul file
print("berita yang tersedia: %s" % title.decode('utf-8'))
print()
download = input("download file? y/n - ")

if download is 'y':
    download_file(title)

pubsub = r.pubsub()  # object pubsub redis

try:
    pubsub.subscribe(["news_channel"])  # subscribe topik pada redsi
    while True:
        for message in pubsub.listen():  # looping akan berhenti hingga ada message baru
            if message['data'] != 1:  # check data != 1
                print("berita baru: %s" % message['data'].decode('utf-8'))
                print()
                if input("download file? y/n - ") is 'y':
                    title = r.get("news")
                    download_file(title)
except KeyboardInterrupt:
    pubsub.close()
    print("exiting")
