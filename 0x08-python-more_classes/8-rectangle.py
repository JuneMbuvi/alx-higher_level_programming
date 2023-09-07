#!/usr/bin/python3
"""creating a class Rectangle"""


class Rectangle:
    """defining public class attributes no. of instncaes & print symbol"""
    number_of_instances = 0
    print_symbol = '#'
    """first we create the attributes of the rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        type(self).number_of_instances += 1

    """use getters and setters to retrieve & access the width"""
    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """use getters and setters to retrieve & access the height"""
    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """defining public instance area"""
    def area(self):
        return (self.__width * self.__height)

    """defining public instance, perimeter"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
            return (0)
        return (2 * (self.__width + self.__height))

    """defining a static method"""
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    """defining the __str__ method"""
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")

        """creating a list to store the #"""
        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    """deining the repr & eval methods"""
    def __repr__(self):
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    """deleting an instance with del"""
    def __del__(self):
        print("Bye rectangle...")

        type(self).number_of_instances -= 1
