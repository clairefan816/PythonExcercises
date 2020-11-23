import time
import random

def main():
    dream_number = random.randint(1, 50)
    counter = 0

    print('Welcome to the Gussing Game!')
    time.sleep(1)

    print('I picked a number between 1 and 50. Try and guess! \n')

    while True:
        
        diff = abs(dream_number - int(input()))
        counter += 1

        if diff > 20:
            msg = 'icy freezing miserable cold'
        elif diff > 13:
            msg = 'extremly cold'
        elif diff > 8:
            msg = 'very cold'
        elif diff > 5:
            msg = 'cold'
        elif diff > 3:
            msg = 'warm'
        elif diff > 2:
            msg = 'very warm'
        elif diff == 2:
            msg = 'extremely warm'
        elif diff == 1:
            msg = 'scalding hot'
        else:
            break
        
        print('Your guess is ', msg)

    print('Congratulations! You figured it out in', counter, 'tries.')
    
    if counter == 1:
        print('That was lucky!')
    elif counter <= 4:
        print('That was amazing!')
    elif counter <= 6:
        print('That was okay.')
    elif counter == 7:
        print('Meh.')
    elif counter <= 9:
        print('This is not your game.')
    else:
        print('You are the worst guesser I\'ve ever seen.')

main()


