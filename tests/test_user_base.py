from unittest import TestCase

from src.user.user import User
from src.user.user_base import UserBase


class TestUserBase(TestCase):
    def test_add_and_get(self):
        capacity = 10
        shift = 20

        user_base = self._make_user_base(capacity)
        users = self._make_users(user_base, capacity + shift)

        missing_user = user_base.get(shift-1)
        existing_user = user_base.get(shift)

        self.assertEqual(missing_user, None)
        self.assertEqual(existing_user, users[shift])

    def test_get_non_existing(self):
        user_base = self._make_user_base(2)
        self._make_users(user_base, 2)

        missing_user = user_base.get(100)
        self.assertEqual(missing_user, None)

    def _make_users(self, user_base, count):
        users = []
        for i in range(count):
            user_base.add(i)
            user = user_base.get(i)
            users.append(user)
        return users

    def _make_user_base(self, capacity):
        return UserBase(capacity)
