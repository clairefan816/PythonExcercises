def my_input(s):
    print(s)
    while True:
        ans = input().lower()
        if ans in ['yes', 'no']:
            return ans
        print("Please say 'yes' or 'no'.")

def ask_if_coughing():
    ans = my_input('Are you coughing? (Yes/No)')
    if ans == 'yes':
        ask_if_short_breath()
    else:
        ask_if_headache_1()

def ask_if_headache_1():
    ans = my_input('Do you have a headache? (Yes/No)')
    if ans == 'yes':
        ask_if_exp()
    else:
        ask_if_ach()

def ask_if_exp():
    ans = my_input('Are you experiencing any of the following: pain when bending your head forward, nausea or vomiting, bright light hurting your eyes, drowsiness or confusion? (Yes/No)')
    if ans == 'yes':
        print('Possibilities include menigitis.')
    else:
        ask_if_vomit()

def ask_if_vomit():
    ans = my_input('Are you vomiting or had diarrhea? (Yes/No)')
    if ans == 'yes':
        print('Possibilities include digestive tract infection.')
    else:
        ask_if_ach()

def ask_if_short_breath():
    ans = my_input('Are you short of breath or wheezing or coughing up phlegm? (Yes/No)')
    if ans == 'yes':
        print('Possibilities include pneumonia or infection of airways.')
    else:
        ask_if_headache_2()


def ask_if_headache_2():
    ans = my_input('Do you have a headache? (Yes/No)')
    if ans == 'yes':
        print('Possibilities include viral infection.')
    else:
        ask_if_ach()

def ask_if_ach():
    ans = my_input('Do you have aching bones or aching joints? (Yes/No)')
    if ans == 'yes':
        print('Possibilities include viral infection.')
    else:
        ask_if_rash()

def ask_if_rash():
    ans = my_input('Do you have a rash? (Yes/No)')
    if ans == 'yes':
        print('Insufficient information to list possibilities.')
    else:
        ask_if_throat()

def ask_if_throat():
    ans = my_input('Do you have a sore throat? (Yes/No)')
    if ans == 'yes':
        print('Possibilities include a throat infection.')
    else:
        ask_if_back()

def ask_if_back():
    ans = my_input('Do you have back pain just above the waist with chills and fever? (Yes/No)')
    if ans == 'yes':
        print('Possibilities include kidney infection.')
    else:
        ask_if_uri()

def ask_if_uri():
    ans = my_input('Do you have pain urinating or are urinating more often? (Yes/No)')
    if ans == 'yes':
        print('Possibilities include a urinary tract infection.')
    else:
        ask_if_sun()

def ask_if_sun():
    ans = my_input('Have you spent the day in the sun or in hot conditions? (Yes/No)')
    if ans == 'yes':
        print('Possibilities sunstroke or heat exhausition.')
    else:
        print('Insufficient information to list possibilities.')

def main():
    ask_if_coughing()

main()