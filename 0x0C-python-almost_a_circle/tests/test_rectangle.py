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
        correct = "[Rectangle] (23) 2/1 - 4/6\n".format(r1.id)
        r2 = Rectangle(5, 5, 1)
        capture = testStdout.capture_output(r1, "print")
        correct = "[Rectangle] (12) 2/1 - 4/6\n".format(r2.id)
        self.assertEqual(correct, capture.getvalue())
        r1 = Rectangle(10, 2, 1, 9)
        capture = testStdout.capture_output(r1, "print")
        correct = "[Rectangle] (1) 1/9 - 10/2\n".format(r1.id)

    """test display with x and y included"""
    def test_dislayOne(self):
        r1 = Rectangle(2, 3, 2, 2)
        capture = testStdout.capture_output(r1, "display")
        self.assertEqual("\n\n  ##\n  ##\n  ##\n", capture.getvalue())
        r2 = Rectangle(3, 2, 1, 0)
        capture = testStdout.capture_output(r2, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    """test for updated arguments"""
    def test_updates(self):
        r1 = Rectangle(10, 10, 10, 10)
        capture = testStdout.capture_output(r1, "print")
        correct = "[Rectangle] (19) 10/10 - 10/10\n".format(r1.id)
        self.assertEqual(correct, capture.getvalue())
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r1))
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r1))
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r1))
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r1))
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r1))

    """test for kwargs"""
    def test_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        capture = testStdout.capture_output(r1, "print")
        correct = "[Rectangle] (1) 10/10 - 10/10\n".format(r1.id)
        r1.update(height=1)
        self.assertEqual("[Rectangle] (16) 10/10 - 10/1", str(r1))
        r1.update(width=1, x=2)
        self.assertEqual("[Rectangle] (16) 2/10 - 1/1", str(r1))
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual("[Rectangle] (89) 3/1 - 2/1", str(r1))
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r1))

class testDictionary:
    """tests the dictionary representation of the Rectangle"""
    def test_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        correct = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r1.to_dicionary)

    """test for rectangle that fails to convert to dictionary representation"""
    def test_dictWithNoChange(self):
        r1 = (10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary())
        self.assertNotEqual(r1, r2)

    """testing the args in the dictionary"""
    def test_dictArg(self):
        r1 = (10, 2, 1, 9)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()
