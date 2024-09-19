import unittest

# classify triangle function
def classify_triangle(a,b,c):
    # wrong input type
    if (type(a) != (int or float)) or (type(b) != (int or float)) or (type(c) != (int or float)):
        return 'WrongInput'
    elif (a < 0) or (b < 0) or (c < 0):
        return 'WrongInput'
    
    # cannot form a triangle
    if (a >= b+c) or (b >= a+c) or (c >= a+b):
        return 'NotATriangle'
    # 2 edges are eaqul
    if a==b or a==c or b==c:
        # if 3 edges are equal then Equilateral
        if a==b and a==c and b==c:
            return 'Equilateral'
        # 2 edges are eaqul and also right triangle
        elif (a*a == (b*b + c*c)) or (b*b == (a*a + c*c)) or (c*c == (a*a + b*b)):
            return 'Right and Isoceles'
        else:
            return 'Isoceles'
    # 3 different edge
    elif a!=b and a!=c and b!=c:
        # Also right triangle
        if (a*a == (b*b + c*c)) or (b*b == (a*a + c*c)) or (c*c == (a*a + b*b)):
            return 'Right'
        else:
            return 'Scalene'


# unitest test cases
class test_triangles(unittest.TestCase):

    def test_Set1(self): 
        self.assertEqual(classify_triangle(3,3,3), 'Equilateral', 'Pass')
        self.assertEqual(classify_triangle(3,4,3), 'Isoceles', 'Pass')
        self.assertEqual(classify_triangle(3,4,6), 'Scalene', 'Pass')
        self.assertEqual(classify_triangle(3,4,5), 'Right', 'Pass')

    def test_Set2(self):
        self.assertEqual(classify_triangle(3,4,7), 'NotATriangle', 'Pass')
        self.assertEqual(classify_triangle(3,4,8), 'NotATriangle', 'Pass')
        self.assertEqual(classify_triangle(1,3,4), 'NotATriangle', 'Pass')
        # a+b = c not a triangle
        self.assertEqual(classify_triangle(0,0,0), 'NotATriangle', 'Pass')

    def test_Set3(self):
        self.assertNotEqual(classify_triangle(10,10,10), 'Isoceles', 'should be Equilateral    Pass')
        self.assertNotEqual(classify_triangle(10,10,5), 'Equilateral', 'should be Isoceles    Pass')
        self.assertNotEqual(classify_triangle(6,8,10), 'Scalene', 'should be Right    Pass')
        self.assertNotEqual(classify_triangle(7,8,10), 'Right', 'should be Scalene    Pass')

    def test_Set4(self):
        # NotANumber input test
        self.assertEqual(classify_triangle('a',10,10), 'WrongInput', 'Pass')
        self.assertEqual(classify_triangle('a','b',10), 'WrongInput', 'Pass')
        self.assertEqual(classify_triangle('a',10,'c'), 'WrongInput', 'Pass')
        self.assertNotEqual(classify_triangle(10,10,10),' WrongInput', 'Pass')

    def test_Set5(self):
        # negitive input test
        # -3 > -4 + -5 seems belongs to NotATriangle, but it should be WrongInput
        self.assertEqual(classify_triangle(-3,-4,-5), 'WrongInput', 'Pass')
        self.assertEqual(classify_triangle(-4,-4,-4), 'WrongInput', 'Pass')
        self.assertNotEqual(classify_triangle(-4,-4,-4), 'NotATriangle', 'should be WrongInput    Pass')
 

if __name__ == '__main__':
    # automatic run all 5 tests
    unittest.main(exit=True)
