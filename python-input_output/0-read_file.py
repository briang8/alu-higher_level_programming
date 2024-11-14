#!/usr/bin/python3
# 0-read_file.py
"""This is a python file that
opens a file for reading and
prints its contents to the standard output
"""
def read_file(filename=""):
    """Reads a text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)

