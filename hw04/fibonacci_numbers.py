import sys

# the sequence should always begin with 0 and 1
sequence_list = [0, 1]


def main(sequence_number):
    """
    print the fibonacci number through for loop
    """
    for i in range(2, sequence_number):
        new_number = sequence_list[i-2] + sequence_list[i-1]
        sequence_list.append(new_number)
    print(sequence_list[0:sequence_number])


main(int(sys.argv[1]))