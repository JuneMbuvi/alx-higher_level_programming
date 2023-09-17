import unittest
from models.base import Base
from models.rectangle import Rectangle
"""tests the subclass Rectangle"""


class testRectangleClass(unittest.TestCase):
    """test whether the rectangle is an instance of the Base class"""
    def test_rect_instances(self):
        r1 = Rectangle(10, 2)
        self.assertIsInstance(Rectangle(10, 2), Base)
        r2 = Rectangle(2, 10)
        self.assertIsInstance(Rectangle(2, 10), Base)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertIsInstance(Rectangle(10, 2, 0, 0, 12), Base)

    """test for type & value errors in the attributes"""
    def test_for_errors(self):
        self.assertRaises(Exception)
    
    """test the values used to calculate area"""
    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

if __name__ == "__main__":
    unittest.main()
