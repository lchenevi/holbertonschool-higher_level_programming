#!/usr/bin/python3

def fizzbuzz():
    # Iterate through the numbers from 1 to 100 (inclusive).
    for i in range(1, 101):
        # Check if the current number is a multiple of both 3 and 5.
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end='')
        # Check if the current number is a multiple of 3 only.
        elif i % 3 == 0:
            print("Fizz", end='')
        # Check if the current number is a multiple of 5 only.
        elif i % 5 == 0:
            print("Buzz", end='')
        # If the current number is not a multiple of 3 or 5, print the
        # number itself.
        else:
            print(i, end='')

        # Print a space after each output for better readability.
        print(" ", end='')

# Call the 'fizzbuzz' function to execute the FizzBuzz logic.
#fizzbuzz()
