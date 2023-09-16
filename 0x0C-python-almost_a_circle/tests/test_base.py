import unittest
from models.base import Base
"""tests the Base class"""


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

if __name__ == "__main__":
    unittest.main()
