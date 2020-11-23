
THRESHOLD = 9


def convert(num1, num2):
    """
    convert the number and count
    num1, num2 -> none
    """
    max_len = len(num1) if len(num1) > len(num2) else len(num2)
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)

    res1 = list(map(int, str(num1)))
    res2 = list(map(int, str(num2)))

    counter = 0
    carry = False
    for i in range(-1, -max_len - 1, -1):
        zum = res1[i] + res2[i] + (1 if carry else 0)
        carry = False
        if zum > THRESHOLD:
            counter += 1
            carry = True
    print(counter)


def main():
    """
    collect the input
    call the functions
    """
    num1 = input('Enter the first number: ')
    num2 = input('Enter the second number: ')
    print(f'{num1} + {num2} = {int(num1)+int(num2)}')
    convert(num1, num2)


main()
