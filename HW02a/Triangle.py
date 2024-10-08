# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def isRightTriangle(a,b,c):
    a_sq = round(a**2, 4)
    b_sq = round(b**2, 4)
    c_sq = round(c**2, 4)

    if (round((a_sq + b_sq), 4) == c_sq) or (round((a_sq + c_sq), 4) == b_sq) or (round((c_sq + b_sq), 4) == a_sq):
        return True
    else:
        return False

def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """

    # verify that all 3 inputs are integers or float
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not( (isinstance(a,int) or isinstance(a,float)) and (isinstance(b,int) or isinstance(b,float)) and (isinstance(c,int) or isinstance(c,float)) ):
        return 'InvalidInput'

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a+b <= c) or (a+c <= b ) or (b+c <= a):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == c and c == a:
        return 'Equilateral'
    elif (a==b) or (a==c) or (b==c):
        if isRightTriangle(a,b,c):
            return 'Isoceles and Right'
        else:
            return 'Isoceles'
    elif (a != b) and  (b != c) and (a != b):
        if isRightTriangle(a,b,c):
            return 'Right'
        else:
            return 'Scalene'
