import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
import sys
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

class testStdout(unittest.TestCase):
    """test that actual output is equal to actual"""
    
    @staticmethod
    def capture_output(rect, method):
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return (capture)

    """print # in stdout"""
    def test_display(self):
        r1 = Rectangle(4, 6)
        capture = testStdout.capture_output(r1, "display")
        self.assertEqual("####\n####\n####\n####\n####\n####\n", capture.getvalue())
        r2 = Rectangle(2, 2)
        capture = testStdout.capture_output(r2, "display")
        self.assertEqual("##\n##\n", capture.getvalue())

    """test the string representation of Rectangle"""
    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        capture = testStdout.capture_output(r1, "print")
        correct = "[Rectangle] (12) 2/1 - 4/6\n".format(r1.id)
        r2 = Rectangle(5, 5, 1)
        capture = testStdout.capture_output(r1, "print")
        correct = "[Rectangle] (12) 2/1 - 4/6\n".format(r2.id)
        self.assertEqual(correct, capture.getvalue())

if __name__ == "__main__":
    unittest.main()
