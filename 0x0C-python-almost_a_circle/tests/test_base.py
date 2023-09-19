import unittest
from models.base import Base
"""tests the Base class"""
from models.rectangle import Rectangle

class TestBaseClass(unittest.TestCase):
    def test_id(self):
        """tests for ids >= 0"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_unique_id(self):
        """b4 = Base()"""
        self.assertEqual(12, Base(12).id)
        b5 = Base()
        self.assertEqual(b5.id, 4)

class Test_to_json_string(unittest.TestCase):
    """validates the output of json string"""
    def test_to_json_string(self):
        """checks whether actual and expected output
        are equal"""
        r = Rectangle(10, 7, 2, 8)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

if __name__ == "__main__":
    unittest.main()
