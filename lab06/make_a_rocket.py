import sys as s
import math as m

WIDTH_ARG_POSITION = 1
SEGMENT_ARG_POSITION = 2
STYLE_ARG_POSITION = 3


def cone(width):
    """
    draw cone part
    width -> None
    """
    row = 0
    height = m.ceil((width-2)/2)
    while row < height:
        print(' ' * int(height - row), end='')
        print('*' * int(row * 2 + 1), end='')
        if width % 2 == 0:
            print(end='*')
        print()
        row += 1


def fulselage(width, style):
    """
    draw fulselage part
    width, default -> None
    """
    row = 0
    height = width
    while row < height:
        # Decide what to print.
        if style == 'striped':
            if row < height/2:
                char = '_'
            else:
                char = 'x'
        else:
            char = style
        # Print one row.
        print(char * width)
        row += 1


def base(width):
    """
    draw the base
    width -> None
    """
    if (width - width//2) % 2 == 0:
        fin_width = width//2

    elif(width - width//2) % 2 != 0:
        fin_width = width//2 - 1

    row = 0
    while row < (width - fin_width) / 2 + 1:
        space = (width - fin_width) / 2 - row
        print(' ' * int(space), end='')
        print('*' * int(fin_width + 2 * row))
        row += 1
    print('*' * width)


def main(argv):
    if not (3 <= len(argv) <= 4):
        print("Usage: python make_a_rocket.py <width> <segments> [style]")
        exit()
    width = int(argv[WIDTH_ARG_POSITION])
    sqr_segement = int(argv[SEGMENT_ARG_POSITION])
    style = argv[STYLE_ARG_POSITION] if len(argv) == 4 else 'x'
    cone(width)
    for _ in range(sqr_segement):
        fulselage(width, style)
    base(width)


main(s.argv)
