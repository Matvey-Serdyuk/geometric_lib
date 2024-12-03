import unittest
import unittest
import datetime


def area(a):
    '''
    Принимает число a, возвращает площадь квадрата со стороной a
    Code:
    print(area(5))
    Output:
    25
    '''
    try:
        a = int(a)
    except ValueError:
        return ValueError
    return a * a


def perimeter(a):
    '''
    Принимает число a, возвращает периметр квадрата со стороной a
    Code:
    print(perimeter(5))
    Output:
    20
    '''
    try:
        a = int(a)
    except ValueError:
        return ValueError
    return 4 * a



class SquareTestCase(unittest.TestCase):
    def test_area1(self):
        self.assertEqual(area(4), 16)
        self.success_message("area(4)", 16)
    
    def test_area2(self):
        self.assertEqual(area("aba"), ValueError)
        self.success_message("area(\"aba\")", ValueError)
    
    def test_area3(self):
        self.assertEqual(area("5"), 25)
        self.success_message("area(\"5\")", 25)
    
    def test_perimeter1(self):
        self.assertEqual(perimeter(3), 12)
        self.success_message("perimeter(3)", 12)
    
    def test_perimeter2(self):
        self.assertEqual(perimeter("rrr"), ValueError)
        self.success_message("perimeter(\"rrr\")", ValueError)
    
    def test_perimeter3(self):
        self.assertEqual(perimeter("8"), 32)
        self.success_message("perimeter(\"8\")", 32)
    
    def success_message(self, func, output):
        print(datetime.datetime.now().strftime('%d-%m-%Y'), end=" ")
        print(datetime.datetime.now().time().isoformat()[:8], end=": ")
        print(self._testMethodName +
               " passed => " + str(func) + " >> " + str(output))