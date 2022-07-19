#!/usr/bin/python3
class Square:

    """ Class Square that defines methods and attributes for a square object"""

    def __init__(self, size=0, position=(0, 0)):
        """ Class Constructor"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Private Attribute size Getter """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Private Attribute size Setter """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ Private Attribute position Getter """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Private Attribute position Setter """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Method that calculates current square area """
        return (self.__size * self.__size)

    def my_print(self):
        """ Method that prints in stdout the square with the char # """
        if self.size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.size):
                print("{}{}".format(' '*self.__position[0], '#'*self.__size))
