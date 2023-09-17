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
    def width(self, value):
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
