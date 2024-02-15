#!/usr/bin/python3
def read_file(filename=""):
    """
    Reads a text file and prints its contents to stdout.

    Args:
        filename (str): The name of the text file to read
        (default is an empty string).

    Returns:
        None
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')  # Print each line without
                                     # adding extra newline characters
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
