import math
def main():
    angle = float(input('Please enter an angle: '))
    cosine_angle = math.cos(math.radians(angle))
    sine_angle = math.sin(math.radians(angle))

    print('The cosine of {} is {}'.format(angle, cosine_angle))
    print('The sine of {} is {}'.format(angle, sine_angle))

main()