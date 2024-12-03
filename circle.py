import math
import unittest
import datetime


def area(r):
    '''
    Принимает число r, возвращает площадь круга радиуса r
    Code:
    print(area(5))
    Output:
    78.53981633974483
    '''
    try:
        r = int(r)
    except ValueError:
        return ValueError
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает число r, возвращает периметр круга радиуса r
    Code:
    print(perimeter(5))
    Output:
    31.41592653589793
    '''
    try:
        r = int(r)
    except ValueError:
        return ValueError
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_area1(self):
        d = area(5) - 3.14 * 5 * 5
        self.assertEqual(d <= 0.1, True)
        self.success_message("area(5)", str(area(5)))
    
    def test_area2(self):
        self.assertEqual(area("r"), ValueError)
        self.success_message("area(\"r\")", str(area("r")))
    
    def test_area3(self):
        d = area("4") - 3.14 * 5 * 5
        self.assertEqual(d <= 0.1, True)
        self.success_message("area(\"4\")", str(area("4")))
    
    def test_perimeter1(self):
        d = perimeter(5) - 3.14 * 5 * 2     
        self.assertEqual(d <= 0.1, True)
        self.success_message("perimeter(5)", str(perimeter(5)))
    
    def test_perimeter2(self):
        self.assertEqual(perimeter("r"), ValueError)
        self.success_message("perimeter(\"r\")", str(perimeter("r")))
    
    def test_perimeter3(self):
        d = perimeter("4") - 3.14 * 5 * 2
        self.assertEqual(d <= 0.1, True)
        self.success_message("perimeter(\"4\")", str(perimeter("4")))
    
    def success_message(self, func, output):
        print(datetime.datetime.now().strftime('%d-%m-%Y'), end=" ")
        print(datetime.datetime.now().time().isoformat()[:8], end=": ")
        print(self._testMethodName +
               " passed => " + str(func) + " >> " + str(output))
