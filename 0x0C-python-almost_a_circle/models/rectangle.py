#!/usr/bin/python3
from models.base import Base
"""creates a subclass Rectangle that inherits from class Base"""


class Rectangle(Base):
    """constructor method"""
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
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """get and set value for height"""
    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """set and get value for x"""
    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """set and get value for y"""
    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self):
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
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str(self.id) + ") "
        string += str(self.__x) + "/" + str(self.__y)
        string += " - " + str(self.__width) + "/" + str(self.__height)
        return (string)

    """assigning argument to te attributes"""
    def update(self, *args, **kwargs):
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
