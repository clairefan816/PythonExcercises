def main():
    word = input('Please enter a word: ').lower()
    word_case = ''

    for c in word:
        if c in 'aeiou':
            word_case += c.upper()
        else:
            word_case += c.lower()

    print('The consonants and vowels in the word are shown: ', word_case)

main()  