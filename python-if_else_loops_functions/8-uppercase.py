#!/usr/bin/python3

# Define a function named 'uppercase' that takes a string as an
# argument
def uppercase(str):
    # Iterate through each character in the string
    for i in range(len(str)):
        # Check if the ASCII code of the current character is in the
        # lowercase range
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            # If it is a lowercase letter, set 'num' to 32
            num = 32
        else:
            # If it is not a lowercase letter, set 'num' to 0
            num = 0
        # Print the uppercase equivalent of the current character
        # using the ASCII code and 'num'.
        print("{:c}".format(ord(str[i]) - num), end='')
    # Print a newline character after processing all characters in the
    # string.
    print()
