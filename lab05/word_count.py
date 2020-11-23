import re


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            # delete the leading and ending spaces and the newline character
            content = (file.read()).strip().replace('\n', ' ')
    except FileNotFoundError:
        print("Can't open ", filename, "for reading.")
        exit()
    return content


def count_words(content):
    count_words = len(content.split())
    print('Words:', count_words)


def count_characters(content):
    characters = content.replace(' ', '')
    print('Characters:', len(characters))


def count_letters_numbers(content):
    letter_and_numbers = re.findall(r'\w', content)
    print('Letters and numbers are:', len(letter_and_numbers))


def main():
    filename = input('Enter the name of txt: ')
    content = read_file(filename)
    count_words(content)
    count_characters(content)
    count_letters_numbers(content)


main()
