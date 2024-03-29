#!/usr/bin/python3
"""Define a text file-reading function."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="Utf-8") as f:
        print(f.read(), end="")
