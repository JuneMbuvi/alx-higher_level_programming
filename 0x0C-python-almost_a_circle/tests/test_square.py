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

    """test for type & value errors in the attributes"""
    def test_for_sqerrors(self):
        self.assertRaises(Exception)

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
        correct = "[Square] (32) 2/0 - 2\n".format(s2.id)
        self.assertEqual(correct, capture.getvalue())
        s3 = Square(3, 1, 3)
        capture = testStdout.capture_output(s3, "print")
        correct = "[Square] (33) 1/3 - 3\n".format(s3.id)
        self.assertEqual(correct, capture.getvalue())

    """test for updated arguments"""
    def test_updates(self):
        s1 = Square(5)
        capture = testStdout.capture_output(s1, "print")
        correct = "[Square] (34) 0/0 - 5\n".format(s1.id)
        self.assertEqual(correct, capture.getvalue())
        s1.update(10)
        self.assertEqual("[Square] (10) 0/0 - 5", str(s1))
        s1.update(1, 2)
        self.assertEqual("[Square] (1) 0/0 - 2", str(s1))
        s1.update(1, 2, 3)
        self.assertEqual("[Square] (1) 3/0 - 2", str(s1))
        s1.update(1, 2, 3, 4)
        self.assertEqual("[Square] (1) 3/0 - 2", str(s1))

    """test for kwargs"""
    def test_kwargs(self):
        s1 = Square(5)
        capture = testStdout.capture_output(s1, "print")
        correct = "[Square] (30) 0/0 - 5\n".format(s1.id)
        self.assertEqual(correct, capture.getvalue())
        s1.update(x=12)
        self.assertEqual("[Square] (30) 12/0 - 5", str(s1))
        s1.update(size=7, y=1)
        self.assertEqual("[Square] (30) 12/0 - 7", str(s1))
        s1.update(size=7, id=89, y=1)
        self.assertEqual("[Square] (89) 12/0 - 7", str(s1))

if __name__ == "__main__":
    unittest.main()
