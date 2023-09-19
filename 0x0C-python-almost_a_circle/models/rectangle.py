#!/usr/bin/python3
"""creates a subclass Rectangle that inherits from class Base"""
from models.base import Base


class Rectangle(Base):
    """constructor method to instatntiate the Rectangle
    Args
    Base - super/parent class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        """to pass the id from the super"""
        Base.__init__(self, id)

    """use getters & setters to access and set values of the attributes
    start with width"""
    @property
    def width(self):
        """returns the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets width of the Rectangle and equates it to value.
        Also validates attributes for correct Type and value
        Arg
        value - value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """get and set value for height"""
    @property
    def height(self):
        """returns height value"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets height of the Rectangle and equates it to value.
        Also validates attributes for correct Type and value
        Arg
        value - value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """set and get value for x"""
    @property
    def x(self):
        """returns x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """sets the x value of the Rectangle and equates it to value.
        Also validates attributes for correct Type and value
        Arg
        value - value of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """set and get value for y"""
    @property
    def y(self):
        """returns y"""
        return (self.__y)

    @y.setter
    def y(self):
        """sets the x value of the Rectangle and equates it to value.
        Also validates attributes for correct Type and value
        Arg
        value - value of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """get area of rectangle"""
    def area(self):
        """returns area of rectangle"""
        return (self.__width * self.__height)

    """public instance display that displays the #"""
    def display(self):
        """prints in stdout the Rectangle in # and
        prints an empty string if width or height is 0"""
        if self.__width == 0 or self.__height == 0:
            print("")
            return

        [print("") for y in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            [print("#", end="") for j in range(self.__width)]
            print("")
            """if the last column is not reached, go to the next line/column
            if i != self.__height - 1:
                rect.append("\n")
        print("".join(rect))"""

    """override the __str__ method"""
    def __str__(self):
        """returns the string representation of Rectangle with its
        atributes"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str(self.id) + ") "
        string += str(self.__x) + "/" + str(self.__y)
        string += " - " + str(self.__width) + "/" + str(self.__height)
        return (string)

    """assigning argument to te attributes"""
    def update(self, *args, **kwargs):
        """assigns arguments or key/value pairs to each attributes
        Args
        args - arguments.
        kwargs - keyword arguments that are used in the absence of
        arguments or in case of an empty class"""
        if args and len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.__width, self.__height,
                                      self.__x, self.__y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.__width = arg
                elif count == 2:
                    self.__height = arg
                elif count == 3:
                    self.__x = arg
                elif count == 4:
                    self.__y = arg
                count += 1

        """if args doesn't exist/ is empty, skip to **kwargs"""
        for key, value in kwargs.items():
            if key == "id":
                if value is None:
                    self.__init__(self.__width, self.__height,
                                  self.__x, self.__y)
                else:
                    self.id = value
            elif key == "width":
                self.__width = value
            elif key == "height":
                self.__height = value
            elif key == "x":
                self.__x = value
            elif key == "y":
                self.__y = value

    """dictionary representation"""
    def to_dictionary(self):
        """translates the attributes to a dictionary representation
        of themselves"""
        return {
                "id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y
                }
