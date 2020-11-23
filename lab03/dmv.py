
import random

def main():
    print('Welcome to the DMV (estimated wait time is 3 hours)')
    full_name = input('Please enter your first, middle, and last name:  \n')
    date_of_birth = input('Enter date of birth (MM/DD/YY):  \n')

    # convert the name into a titlecased version
    full_name = full_name.title()

    driver_license = ''
    for i in range(0,7):
        driver_license += str(random.randrange(0, 9))

    last_name = full_name[full_name.rfind(' ') + 1:]
    first_middle_name = full_name[:full_name.rfind(' ')]

    month, day, year = date_of_birth.split('/')

    print('---------------------------------------------------------')
    print('Washington Driver License')
    print('DL ', driver_license)
    print('LN ', last_name)
    print('FN ', first_middle_name)
    print('DOB {}/{}/{}'.format(month, day, year))
    print('EXP {}/{}/21'.format(month, day))
    print('---------------------------------------------------------')

main()