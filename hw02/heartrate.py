
def main():

    # get the inputs from user
    age = int(input("Please enter your age: "))
    restHR = int(input("Please enter your resting heart rate: "))
    PRECISION = 2

    print("=======================================")
   
    # An euqation commonly used in medicine
    max_heart_rate = 208 - 0.7 * age
    reserve = max_heart_rate - restHR
    
    print('Your hear rate reserve is: ', round(reserve, PRECISION), 'bpm ' )
    print('Here is a breakdown of your training zone:')

    # %.2f refers to the precision of the float value
    print('zone 1: %.2f to %.2f bpm' % (restHR + reserve*0.5, restHR + reserve*0.6))
    print('zone 1: %.2f to %.2f bpm' % (restHR + reserve*0.6, restHR + reserve*0.7))
    print('zone 1: %.2f to %.2f bpm' % (restHR + reserve*0.7, restHR + reserve*0.8))
    print('zone 1: %.2f to %.2f bpm' % (restHR + reserve*0.8, restHR + reserve*0.93))
    print('zone 1: %.2f to %.2f bpm' % (restHR + reserve*0.93, restHR + reserve*1))
    
    print("=======================================")


main()