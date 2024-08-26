#!/usr/bin/env python3
"""Module to test utils file"""
from parameterized import parameterized
import unittest
from unittest.mock import patch


def access_nested_map(nested_map, path):
    """Access a nested dictionary with a sequence of keys.

    Args:
        nested_map (dict): The nested dictionary to access.
        path (tuple): A sequence of keys to access the nested dictionary.

    Returns:
        The value associated with the given path in the nested dictionary.

    Raises:
        KeyError: If the given path is invalid or does not exist in the
            nested dictionary.
    """
    for key in path:
        if not isinstance(nested_map, dict) or key not in nested_map:
            raise KeyError(key)
        nested_map = nested_map[key]
    return nested_map


def get_json(url):
    """Fetch JSON data from a remote URL.

    Args:
        url (str): The URL to fetch JSON data from.

    Returns:
        The JSON data retrieved from the remote URL.
    """
    import requests
    response = requests.get(url)
    return response.json()


def memoize(func):
    """Memoize the result of a function call for given arguments.

    Args:
        func (callable): The function to be memoized.

    Returns:
        A wrapped function that caches and returns the result of
        calling the original function with the same arguments.
    """
    cache = {}

    def wrapped(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapped


class TestAccessNestedMap(unittest.TestCase):
    """Test class for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns the expected value."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test that access_nested_map raises KeyError for invalid paths."""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))


class TestGetJson(unittest.TestCase):
    """Test class for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test that get_json returns the expected JSON data."""
        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()


class TestMemoize(unittest.TestCase):
    """Test class for the memoize decorator."""

    def test_memoize(self):
        """Test memoization of a function call.

        Ensure that when calling a_property twice, the correct result
        is returned but a_method is only called once, as verified by
        assert_called_once.
        """

        class TestClass:
            """Test class for wrapping a method with memoize."""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
