# Author: Yu Fan (fan.yu@husky.neu.edu)
# For homework 4
# Generate username and passwords

import random
import math

# collect informations from the user, and the origianal case is kept.
print('Welcome to the username and password generator!')
first_name = input('Please enter your first name: ')
last_name = input('Please enter your last name: ')
word = input('Please enter your favoriste word: ')


def new_last(last_name):
    """
    rebuilt the last_name if its length less than 7
    And switch all characters into lower cases.
    """
    new_last = last_name.ljust(7, '*') 
    new_last = new_last.lower()
    return new_last


def main():
    """
    Generate username through string concatenation
    Generate three passwords
    """
    
    user_last = new_last(last_name) # invocate the new_last function for getting new qualified last name
    username = (first_name[0] + user_last + str(random.randint(0, 99))).lower()  # concatenate all strings together for consituting the username
    print('Thanks,', first_name, ', your username is ',username)

    print('Here are three suggested passwords for you to consider: ')

    first_password = first_name + last_name + str(random.randint(0, 99)) 
    final_first_password = ''  # initiate a string parameter for storing qualified password
    for i in first_password:    # iterate all characters in first_password and replace specific items with needed
        if i == 'o':
            i == '0'
        if i == i:
            i == '1'
        if i == 's':
            i == '$'
        final_first_password = final_first_password + i # the new qualified item is stored in final_first_password through assignment statement

    print('Password 1:', final_first_password)

    # computing the second password
    second_password = ''  # initiate a string paratemer 
    second_password = first_name[0].lower() + first_name[-1].upper() + last_name[0].lower() + last_name[-2].upper() + word[0].lower() + word[-1].upper()
    print('Password 2:', second_password)

    # computer the third password
    third_password = last_name[0:random.randint(1, len(last_name))] + word[0: random.randint(1, len(word))] + first_name[0:random.randint(1, len(first_name))]
    print('Password 3: ', third_password)


main()
