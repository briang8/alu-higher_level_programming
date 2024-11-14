#!/usr/bin/python3
# 1-write_file.py
"""This is a python file that
writes to a file, creates the file
if it doesn't exist,it also
overwrites the content of the file if
it exists
"""


def write_file(filename="", text=""):
    """This  function creates the file and writes into
    it and makes sure a new line is
    appended to the end of the string
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        # if text[len(text) - 1] != "\n": text += "\n"
        num_char_written = f.write(text)
        return num_char_written
