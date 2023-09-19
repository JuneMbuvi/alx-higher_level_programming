#!/usr/bin/python3
"""defines a class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """constructor method
    Args
    Rectangle - super/parent class of Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """inherit attributes from the super or Rectangle class"""
        super().__init__(size, size, x, y, id)

    """public getter & setter size"""
    @property
    def size(self):
        """returns the size of square as either
        width/ height since size=width=height"""
        return (self.width)

    @size.setter
    def size(self, value):
        """sets the size of square by equating it to
        its corresponding value
        Args
        value - value of Square"""
        self.width = value
        self.height = value

    """define the square's string representation"""
    def __str__(self):
        """returns the string representation of Square
        and its attributes"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str(self.id) + ") "
        string += str(self.x) + "/" + str(self.y)
        string += " - " + str(self.width)
        return (string)

    """update with args and kwargs"""
    def update(self, *args, **kwargs):
        """updates the square by setting arguments or key/value
        pairs to its attributes
        Args
        args - arguments
        kwargs - keyword arguments which are used only in the absence of
        args/ if args is empty"""
        if args and len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.width = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.__y = arg
                count += 1

        """if args doesn't exist/ is empty, skip to **kwargs"""
        for key, value in kwargs.items():
            if key == "id":
                if value is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    self.id = value
            elif key == "size":
                self.size = value
            elif key == "height":
                self.height = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.__y = value

    """define the dictionary representation of Square"""
    def to_dictionary(self):
        """returns the dictionary representation of the Square"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
