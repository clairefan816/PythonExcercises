import sys


def main(number):
    """
    Print out the triangualr number
    """
    # triangle number (n(n+1)//2)
    tri_number = (number * (number + 1)) / 2
    print(int(tri_number))


main(int(sys.argv[1]))
