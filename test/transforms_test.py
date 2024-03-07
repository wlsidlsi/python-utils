import unittest

from python_utilities.src import transforms

class TestTransforms(unittest.TestCase):
    def test_transforms(self):
        self.assertDictEqual(transforms.find_and_transform(
                data={ "name": { "string" : "my name" }}, 
                key_path="name", 
                transform=lambda i: i["string"]
            ), { "name": "my name" }
        )
        self.assertDictEqual(transforms.find_and_transform(
                data={ "name": "richard" }, 
                key_path="name", 
                transform=lambda i: { "first name": "richard" }
            ), { "name": { "first name" : "richard" } }
        )

    def test_transforms_with_nested(self):
        self.assertDictEqual(transforms.find_and_transform(
                data={ "name": { "string" : { "first": "my name" }}}, 
                key_path="name.string", 
                transform=lambda i: i["first"]
            ), { "name": { "string" : "my name" }}
        )
            