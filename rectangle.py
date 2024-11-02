import unittest


def area(a, b):
    '''
    Принимает числа a и b, возвращает площадь прямоугольника со сторонами a и b
    Code:
    print(area(4, 6))
    Output:
    24
    '''
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return ValueError
    return a * b

def perimeter(a, b):
    '''
    Принимает числа a и b, возвращает периметр прямоугольника со сторонами a и b
    Code:
    print(perimeter(4, 6))
    Output:
    20
    '''
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return ValueError
    return a * 2 + b * 2


class RectangleTestCase(unittest.TestCase):
    def test_area1(self):
        self.assertEqual(area(5, 4), 20)
        self.success_message("area(5, 4)", 20)

    def test_area2(self):
        self.assertEqual(area("r", 3), ValueError)
        self.success_message("area(\"r\", 3)", ValueError)
    
    def test_area3(self):
        self.assertEqual(area("5", "2"), 10)
        self.success_message("area(\"5\", \"2\")", 10)
    
    def test_perimeter1(self):
        self.assertEqual(perimeter(3, 4), 14)
        self.success_message("perimeter(3, 4)", 14)
    
    def test_perimeter2(self):
        self.assertEqual(perimeter(3, "abacaba"), ValueError)
        self.success_message("perimeter(3, \"abacaba\")", ValueError)

    def test_perimeter3(self):
        self.assertEqual(perimeter("5", 6), 22)
        self.success_message("perimeter(\"5\", 6)", 22)
    
    def success_message(self, func, output):
        print(self._testMethodName + " passed >> " + str(func) + " >> " + str(output))