#!/usr/bin/python3
"""
Using a JSON representation, writes an Object to a text file.


"""


import json


def save_to_json_file(my_obj, filename):
    """
    Using a JSON representation, writes an Object to a text file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return (json.dump(my_obj, f))
