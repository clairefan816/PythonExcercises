import math
def main():
    x1 = float(input('Please enter the x value of the first point: '))
    y1 = float(input('Please enter the y value of the first point: '))
    x2 = float(input('Please enter the x value of the second point: '))
    y2 = float(input('Please enter the y value of the second point: '))

    sum1 = (x1 - x2)**2 + (y1 - y2)**2
    distance_of_points = math.sqrt(sum1)

    print('The Euclidean distance between the two points is', distance_of_points)

main()

    