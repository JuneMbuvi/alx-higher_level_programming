#!/usr/bin/python3
"""defines a class MyInt that inherits from int"""


class MyInt(int):
    """inverts the operators != and =="""
    def __eq__(self, value):
        """eq is the function for equal to
        so we override it with the not equal to"""
        return (self.real != value)

    """create the not equal to function"""
    def __ne__(self, value):
        """overrides the ne with the eq operator"""
        return (self.real == value)
