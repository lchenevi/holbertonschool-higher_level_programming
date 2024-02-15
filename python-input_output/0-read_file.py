#!/usr/bin/python3
"""Reads a text file and prints its contents to stdout."""


def read_file(filename=""):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')  # Print each line without
                                     # adding extra newline characters
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
