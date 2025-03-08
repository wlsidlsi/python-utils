#!/usr/bin/env python3
import unittest
import sys
import os
# Add project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.NestedDict import NestedDict


class TestNestedDict(unittest.TestCase):
    def test_nested_getitem(self):
        tests = {
            "a.b": (1, {"a": {"b": 1}}),
            "a.b.c": (2, {"a": {"b": {"c": 2}}}),
            "x.y.z": (3, {"x": {"y": {"z": 3}}}),
            "user.profile.name": ('Chris', {"user": {"profile": {"name": "Chris"}}}),
            "settings.theme.mode": ('dark', {"settings": {"theme": {"mode": "dark"}}}),
            "level1.level2.level3.level4": ('deep', {"level1": {"level2": {"level3": {"level4": "deep"}}}}),
            "config.db.host": ('localhost', {"config": {"db": {"host": "localhost"}}}),
            "system.os.version": ('10.15.7', {"system": {"os": {"version": "10.15.7"}}}),
            "data.items.count": (42, {"data": {"items": {"count": 42}}}),
            "meta.created_at": ('2025-03-08', {"meta": {"created_at": "2025-03-08"}}),
        }

        for key_path, (expected, nested_data) in tests.items():
            with self.subTest(key_path=key_path):
                nested_dict = NestedDict(nested_data)
                self.assertEqual(nested_dict[key_path], expected)

    def test_nested_mutate_at(self):
        data = {"user": {"profile": {"name": "Chris", "age": 35}}}
        nested_dict = NestedDict(data)

        nested_dict.mutate_at("user.profile.age", lambda x: x + 1)
        self.assertEqual(nested_dict["user.profile.age"], 36)

        nested_dict.mutate_at("user.profile.name", lambda x: x.upper())
        self.assertEqual(nested_dict["user.profile.name"], "CHRIS")

        # Test mutating non-existent path (should not raise error)
        nested_dict.mutate_at("user.profile.location.city", lambda x: "Frisco")
        self.assertIsNone(nested_dict["user.profile.location.city"])

    def test_setitem(self):
        data = {}
        nested_dict = NestedDict(data)

        nested_dict["a.b.c"] = 123
        self.assertEqual(nested_dict["a.b.c"], 123)

        nested_dict["x.y"] = "test"
        self.assertEqual(nested_dict["x.y"], "test")

        nested_dict["new.path.to.value"] = True
        self.assertEqual(nested_dict["new.path.to.value"], True)


if __name__ == '__main__':
    unittest.main()

