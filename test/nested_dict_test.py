# create a test cases for src/NestedDict.py
import unittest
from python_utilities.src.NestedDict import NestedDict


class TestNestedDict(unittest.TestCase):
    def test_nested_dict(self):

        # 10 testcases in the form of "a.b": (1, { "a": { "b": 1 }}) each
        # key is a key path representing levels and values nested dicionaries
        
        # create a dictionary of 10 extensive testcases
        tests = {
            "a.b": (1, {"a": {"b": 1}}),
            "a.b": (1, {"a": {"a": 2, "b": 1}}),
            "a.b.c": (2, {"a": {"b": {"c": 2}}}),
            "a.b.c.d": (3, {"a": {"b": {"c": {"d": 3}}}}),
            "a.b.c.d.e": (4, {"a": {"b": {"c": {"d": {"e": 4}}}}}),
            "a.b.c.d.e.f": (5, {"a": {"b": {"c": {"d": {"e": {"f": 5}}}}}}),
            "a.b.c.d.e.f.g": (6, {"a": {"b": {"c": {"d": {"e": {"f": {"g": 6}}}}}}}),
            "a.b.c.d.e.f.g.h": (7, {"a": {"b": {"c": {"d": {"e": {"f": {"g": {"h": 7}}}}}}}})
        }

        for k, v in tests.items():
            nested_dict = NestedDict(v[1])
            self.assertEqual(nested_dict[k], v[0])

