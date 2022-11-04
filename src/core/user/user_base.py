import collections

from src.core.user.user import User


class UserBase:
    """
    A store of id mappings to a User object.
    """

    def __init__(self, capacity=1000):
        # TODO: make it possible to initialize users storage manually
        self.capacity = capacity
        self.users = collections.OrderedDict()

    def add(self, user_id):
        try:
            self.users.pop(user_id)
        except KeyError:
            if len(self.users) >= self.capacity:
                self.users.popitem(last=False)

        user = User(user_id)
        self.users[user_id] = user
        return user

    def get(self, user_id):
        if not self.exists(user_id):
            return None

        value = self.users.pop(user_id)
        self.users[user_id] = value
        return value

    def exists(self, user_id):
        return user_id in self.users
