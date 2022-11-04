class Storage:
    def __init__(self):
        self.storage = {}

    async def add_entry(self, key, value):
        self.storage[key] = value

    async def get_entry(self, key):
        return self.storage[key]
