def take_in_value():
    symbol = str(input('Please enter a symbol you like: '))
    while True:
        width = int(input('Please enter the width of the rectangle: '))
        height = int(input('Please enter the height of the rectangle: '))
        if width >= 2 and height >= 2:
            break
        print('Value is too small!')
    return symbol, width, height


def wide(width, symbol):
    for i in range(width):
        print(symbol, end='')


def main():
    symbol, width, height = take_in_value()
    for h in range(height):
        if h == 0 or h == height - 1:
            wide(width, symbol)
            print()
        else:
            print(symbol, end='')
            wide(width - 2, ' ')
            print(symbol)


main()
