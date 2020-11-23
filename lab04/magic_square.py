puzzle_size = 3


def collect_information():
    list_lines = []
    print('Ener a magic number (please enter three digits): ')
    for i in range(puzzle_size):
        line = input()
        list_lines.append([int(c) for c in line])
    return list_lines


# if magic, return true else return false.
def validator(list_lines):
    for i in range(puzzle_size):
        if sum(list_lines[i]) != 15:
            return False
        if list_lines[0][i] + list_lines[1][i] + list_lines[2][i] != 15:
            return False
    if list_lines[0][0] + list_lines[1][1] + list_lines[2][2] != 15:
        return False
    if list_lines[0][2] + list_lines[1][1] + list_lines[2][0] != 15:
        return False
    return True


def main():
    list_lines = collect_information()
    if validator(list_lines):
        print('It is a magic square!')
    else:
        print('Not a magic square!')


main()
