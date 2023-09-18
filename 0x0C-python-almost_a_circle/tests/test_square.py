import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import io
import sys
"""tests the subclass Rectangle"""

class testClassSquare(unittest.TestCase):
    """test the values used to calculate area"""
    def testsq_area(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        s2 = Square(2, 2)
        self.assertEqual(s2.area(), 4)
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.area(), 9)

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

    """display # in stdout"""
    def test_display(self):
        s1 = Square(5)
        capture = testStdout.capture_output(s1, "display")
        self.assertEqual("#####\n#####\n#####\n#####\n#####\n", capture.getvalue())
        s2 = Rectangle(2, 2)
        capture = testStdout.capture_output(s2, "display")
        self.assertEqual("##\n##\n", capture.getvalue())
        s3 = Square(3, 1, 3)
        capture = testStdout.capture_output(s3, "display")
        self.assertEqual("\n\n\n ###\n ###\n ###\n", capture.getvalue())

    """print # in stdout"""
    def test_str(self):
        s1 = Square(5)
        capture = testStdout.capture_output(s1, "print")
        correct = "[Square] (1) 0/0 - 5\n".format(s1.id)
        s2 = Square(2, 2)
        capture = testStdout.capture_output(s2, "print")
        correct = "[Square] (30) 2/0 - 2\n".format(s2.id)
        self.assertEqual(correct, capture.getvalue())
        s3 = Square(3, 1, 3)
        capture = testStdout.capture_output(s3, "print")
        correct = "[Square] (31) 1/3 - 3\n".format(s3.id)
        self.assertEqual(correct, capture.getvalue())
