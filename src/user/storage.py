

class Storage:
    def __init__(self):
        self.storage = {}

    def add_entry(self, key, value):
        self.storage[key] = value

    def get_entry(self, key):
        return self.storage[key]