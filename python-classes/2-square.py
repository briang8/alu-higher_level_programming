#!/usr/bin/python3
# 2-square.py
class Square:
    def __init__(self, size=0):
        # Check if size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        # Check if size is non-negative
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size  # Set the private instance attribute
