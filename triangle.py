import unittest


def area(a, h):
    '''
    Принимает числа a и h, возвращает площадь треугольника с
      основанием a и высотой h
    Code:
    print(area(4, 7))
    Output:
    14.0
    '''
    try:
        a = int(a)
        h = int(h)
    except ValueError:
        return ValueError
    return a * h / 2 

def perimeter(a, b, c):
    '''
    Принимает числа a, b и c, возвращает периметр треугольника со
      сторонами a, b и c
    Code:
    print(perimeter(2, 3, 4))
    Output:
    9
    '''
    try:
        a = int(a)
        b = int(b)
        c = int(c)
    except ValueError:
        return ValueError
    return a + b + c 


class RectangleTestCase(unittest.TestCase):
    def test_area1(self):
        self.assertEqual(area(5, 4), 10)
        self.success_message("area(5, 4)", 10)
    
    def test_area2(self):
        self.assertEqual(area("b", "a"), ValueError)
        self.success_message("area(\"b\", \"a\")", ValueError)
    
    def test_area3(self):
        self.assertEqual(area("5", 2), 5)
        self.success_message("area(\"5\", 2)", 5)

    def test_perimeter1(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.success_message("perimeter(3, 4, 5)", 12)
    
    def test_perimeter2(self):
        self.assertEqual(perimeter("a", 5, "c"), ValueError)
        self.success_message("perimeter(\"a\", 5, \"c\")", ValueError)
    
    def test_perimeter3(self):
        self.assertEqual(perimeter("6", "7", 8), 21)
        self.success_message("perimeter(\"6\", \"7\", 8)", 21)
    
    def success_message(self, func, output):
        print(self._testMethodName + " passed >> " + str(func) + " >> " + str(output))