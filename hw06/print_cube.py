def draw_corner(size, character1, character2):
    print(end=character1)
    for i in range(2*size):
        print(end=character2)
    print(end=character1)


def leftpart(size, row):
    WHOLE_LEN = (3*size + 6)//2
    HALF_SIZE = size//2

    if row == 1 or row == HALF_SIZE + 2:
        print(' ' * (HALF_SIZE - row + 2), end='')
        draw_corner(size, '+', '-')
    elif 1 < row < HALF_SIZE + 2:
        print(' ' * (HALF_SIZE - row + 2), end='')
        draw_corner(size, '/', ' ')
    elif HALF_SIZE + 2 < row < WHOLE_LEN:
        draw_corner(size, '|', ' ')


def rightpart(size, row):
    WHOLE_LEN = (3*size + 6)//2
    HALF_SIZE = size//2

    if 1 < row <= HALF_SIZE + 1:
        print(' ' * (row - 2), end='')
        print(end='|')
    elif HALF_SIZE + 1 < row <= size + 1:
        print(' '*HALF_SIZE, end='|')
    elif row == size + 2:
        print(' '*HALF_SIZE, end='+')
    elif size + 2 < row <= size + 2 + HALF_SIZE:
        print(' '*(size + 2 + HALF_SIZE - row), end='/')


def main():
    size = int(input('Please input cube size (multiple of 2): '))
    WHOLE_LEN = (3*size + 6)//2
    row = 1
    while row < WHOLE_LEN:
        leftpart(size, row)
        rightpart(size, row)
        print()
        row += 1
    draw_corner(size, '+', '-')


main()
