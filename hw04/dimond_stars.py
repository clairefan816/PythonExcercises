import sys
import math


def main(height):
    # When n is positive integer
    # ceiling(n/2) == (n+1) // 2
    # floor(n/2) == (n-1) // 2

    upper_h = math.ceil(height / 2)
    lower_h = math.floor(height / 2)
    for row in range(upper_h):
        print(' ' * (upper_h - row - 1), ('*' * (2 * row + 1)))
    for row in range(lower_h):   
        print(' ' * (row + upper_h - lower_h), '*' * (2 * lower_h - 2 * row - 1))


main(int(sys.argv[1]))
