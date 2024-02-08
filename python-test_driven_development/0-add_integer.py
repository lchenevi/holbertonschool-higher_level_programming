def add_integer(a, b=98):
    '''
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number. Defaults to 98.

    Returns:
        int: The addition of a and b as integers.
    '''
    # Check if a is an integer or float
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer or b must be an integer')
    # Check if b is an integer or float
    if not isinstance(b, (int, float)):
        raise TypeError('a must be an integer or b must be an integer')

    # Cast a and b to integers if they are float
    a = int(a)
    b = int(b)

    # Return the addition of a and b as integers
    return a + b
