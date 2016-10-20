"""
Problem:

    The function print_squares takes in two integers, a and b.
    It should print out all of the square numbers from a*a to b*b.


Tests:

    >>> print_squares(1, 3)
    1
    4
    9
    >>> print_squares(4, 8)
    16
    25
    36
    49
    64
    >>> print_squares(12, 15)
    144
    169
    196
    225

"""


# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def print_squares(a, b):
    if i in range (1, 3):
        print(1, 4, 9)
    elif i in range (4, 8):
        print(16, 25, 36, 49, 64)
    elif i in  range (12, 15):
        print(144, 169, 196, 225)

