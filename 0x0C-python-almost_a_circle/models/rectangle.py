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
    def setWidth(self):
        self.__width = width

    """get and set value for height"""
    @property
    def height(self):
        return (self.__height)

    @height.setter
    def setHeight(self):
        self.__height = height

    """set and get value for x"""
    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self):
        self.__x = x

    """set and get value for y"""
    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self):
        self.__y = y
