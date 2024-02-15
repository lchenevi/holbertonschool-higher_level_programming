#!/usr/bin/python3
"""Reads a text file and prints its contents to stdout."""


def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')  # Print each line without
                                 # adding extra newline characters
