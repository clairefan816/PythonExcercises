def triangular_number(number):
    """
    calculate the triangular number
    number -> tri_number
    """
    tri_number = int(int(number) * (int(number) + 1) / 2)
    return tri_number


def main():
    """
    Print out the triangualr number
    """
    number = input("Enter a number, or enter 'done':")
    tri_list = []

    while number != 'done':
        tri_number = triangular_number(number)
        print(f'The triangular number for {int(number)} is {tri_number}')
        tri_list.append(tri_number)

        number = input("Enter another number, or enter 'done': ")

    print(tri_list)


main()
