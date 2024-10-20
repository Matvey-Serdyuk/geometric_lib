import math


def area(r):
    '''
    Принимает число r, возвращает площадь круга радиуса r
    Code:
    print(area(5))
    Output:
    78.53981633974483
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает число r, возвращает периметр круга радиуса r
    Code:
    print(perimeter(5))
    Output:
    31.41592653589793
    '''
    return 2 * math.pi * r
