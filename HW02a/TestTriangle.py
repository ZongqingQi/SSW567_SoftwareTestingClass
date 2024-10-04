# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
import math
from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    # Right Triangles
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5,4,3),'Right','5,4,3 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(4,3,5),'Right','4,3,5 is a Right triangle')

    # Isoceles Triangles
    def testIsocelesTrianglesA(self):
        self.assertEqual(classifyTriangle(5,6,5),'Isoceles','5,6,5 should be Isoceles')

    def testIsocelesTrianglesB(self):
        self.assertEqual(classifyTriangle(5.5,6.1,5.5),'Isoceles','5.5,6.1,5.5 should be Isoceles')

    # Isoceles and Right Triangles
    def testIsocelesRightTriangles(self):
        self.assertEqual(classifyTriangle(math.sqrt(2),math.sqrt(2),2),'Isoceles and Right','2**(1/2), 2**(1/2), 2 should be Isoceles')

    # Equilateral Triangles  
    def testEquilateralTrianglesA(self):
        self.assertEqual(classifyTriangle(2,2,2),'Equilateral','2,2,2 should be equilateral')

    def testEquilateralTrianglesB(self):
        self.assertEqual(classifyTriangle(2.5,2.5,2.5),'Equilateral','2.5,2.5,2.5 should be equilateral')

    def testEquilateralTrianglesC(self):
        self.assertEqual(classifyTriangle(math.sqrt(2), math.sqrt(2), math.sqrt(2)),'Equilateral','2**(1/2), 2**(1/2), 2**(1/2) should be equilateral')

    # test Scalene Triangle
    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(7,8,9),'Scalene','7,8,9 is a Scalene triangle')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(7.5,8.5,9.5),'Scalene','7.5,8.5,9.5 is a Scalene triangle')

    def testScaleneTriangleC(self):
        self.assertEqual(classifyTriangle(1.5,8,9),'Scalene','1.5,8,9 is a Scalene triangle')

    # Not A triangle
    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1,2,8),'NotATriangle','1,2,8 is not a triangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(1,8,9),'NotATriangle','1,8,9 is not a triangle')

    # Invalid Input
    def testInvalidInputA(self): # pass with org version
        self.assertEqual(classifyTriangle(-1,-1,-1),'InvalidInput','-1,-1,-1 is a InvalidInput')

    def testInvalidInputB(self): # pass with org version
        self.assertEqual(classifyTriangle(-1,1,1),'InvalidInput','-1,1,1 is a InvalidInput')

    def testInvalidInputC(self): # pass with org version
        self.assertEqual(classifyTriangle(1000,1000,1000),'InvalidInput','1000,1000,1000 is a InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

