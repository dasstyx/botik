from unittest import TestCase

from src.core.navigation.navigation import Navigation


class TestNavigation(TestCase):
    def test_concat_paths_absolute(self):
        expected = '/root/foo/bar'
        result = Navigation.concat_paths('root2/baz', '~/root/foo/bar')
        self.assertEqual(result, expected)

    def test_concat_paths_relative(self):
        expected = '/root/foo/baz'
        result = Navigation.concat_paths('root/foo/bar/b', '../../baz')
        self.assertEqual(result, expected)

    def test_concat_paths_absolute_empty(self):
        expected = '/'
        result = Navigation.concat_paths('', '~')
        self.assertEqual(result, expected)
