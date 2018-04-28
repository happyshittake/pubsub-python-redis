import persistent


class News(persistent.Persistent):
    def __init__(self):
        self.data = []

    def append(self, title):
        self.data.append(title)
