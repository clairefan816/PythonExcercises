LUHN = 10


def get_the_number():
    """input - > list"""
    # get the input from user
    numbers = input("Enter the test number: ")
    # convert the input string to list and reverse the list
    return list(reversed([int(x) for x in numbers]))


def built_new_list(value_list):
    """list -> list"""

    # double every second value
    double_second = [i*2 for i in value_list[1::2]]

    for i in range(len(double_second)):
        a = double_second[i]
        if a > 9:
            double_second[i] = (a % 10 + a//10)
    return double_second


def main():
    value_list = get_the_number()
    remain_list = value_list[::2]
    sum_digits = sum(built_new_list(value_list) + remain_list)
    if (sum_digits % LUHN) == 0:
        print('It is a valid number.')
    else:
        print('It is not a valid number.')


main()
