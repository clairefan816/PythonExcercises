import math
import sys


def one_row(radius, row):
    for column in range(2*radius):
        # we have odd rows and columns, the actural center is between radius - 1 and radius, so we pick radius - 0.5 as the center
        center = radius - 0.5   
        # is (row, column) inside a circle or not?
        if math.sqrt((center - row)**2 + (center - column)**2) > radius:
            print(end=' ')
        else:
            print('o', end='')


def main(radius):
    for i in range(2*radius):
        one_row(radius, i)
        print()


main(int(sys.argv[1]))
