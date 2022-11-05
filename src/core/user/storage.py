class Storage:
    def __init__(self):
        self._storage = {}

    async def set(self, key, value):
        self._storage[key] = value

    async def get(self, key):
        return self._storage[key]
