#!/usr/bin/python3
"""
This module contains a function to read a text file
and print its contents to standard output.
"""

def read_file(filename=""):
    """Reads a text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.

    """
    # Open the specified file in read mode with UTF-8 encoding
    with open(filename, 'r', encoding='utf-8') as file:
        # Read the entire content of the file into a string
        content = file.read()
        
        # Print the content to standard output
        print(content)
