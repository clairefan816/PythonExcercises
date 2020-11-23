
def n_times_c(n, c):
    """
    Print repeating pattern
    """
    for i in range(n):
        print(end=c)


def tree(height):
    """
    Draws a tree of a given width.
    """
    for row in range(height):
        # print leading spaces
        n_times_c(height - row - 1, ' ')

        if row == 0:
            n_times_c(1, '*')
        elif row < height - 1:
            n_times_c(1, '/')
            n_times_c(2 * row - 1, ' ')
            n_times_c(1, '\\')
        else:
            n_times_c(1, '/')
            n_times_c(2 * row - 1, '_')
            n_times_c(1, '\\')
        print()


def main():
    """
    Allows users to draw trees of various width
    """
    while True:
        width = int(input('Enter width of base:  '))
        if width >= 3 and width % 2:
            break
        print('Please input an odd number greater than 2')
    height = int((width + 1) / 2)
    tree(height)


main()
