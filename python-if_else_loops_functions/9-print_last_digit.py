#!/usr/bin/python3

# Define a function named 'print_last_digit' that takes an integer
# 'number' as an argument.
def print_last_digit(number):
    # Check if 'number' is non-negative.
    if number >= 0:
        # If non-negative, calculate the last digit using modulo 10.
        l_digit = number % 10
    else:
        # If negative, calculate the last digit using modulo -10 and
        # make it positive.
        l_digit = number % -10
        l_digit *= -1

    # Print the last digit using the specified format.
    print("{:d}".format(l_digit), end='')

    # Return the last digit.
    return l_digit
