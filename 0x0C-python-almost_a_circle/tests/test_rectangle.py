import unittest
from models.base import Base
from models.rectangle import Rectangle
"""tests the subclass Rectangle"""


class testRectangleClass(unittest.TestCase):
    """test the id of a rectangle"""
    def test_rect_instances(self):
        r1 = Rectangle(10, 2)
        self.assertIsInstance(Rectangle(10, 2), Base)
        r2 = Rectangle(2, 10)
        self.assertIsInstance(Rectangle(2, 10), Base)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertIsInstance(Rectangle(10, 2, 0, 0, 12), Base)

if __name__ == "__main__":
    unittest.main()
