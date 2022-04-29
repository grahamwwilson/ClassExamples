# quadraticMethods.py

# See "How (Not) to Solve Quadratic Equations", Yves Nievergelt, 
# The College Mathematics Journal, 34 (2003) 90-104.
# Available at https://www.jstor.org/stable/3595780
#
# Graham W. Wilson, 28-APR-2022

import cmath              # Allows for complex numbers
import math

def Discriminant(a,b,c):
    d = b**2 - 4*a*c
    return d

def RealSqrt(x):
    assert x >=0, 'Only non-negative discriminants are allowed by math.sqrt'
    return math.sqrt(x)
    
def ComplexSqrt(x):
    return cmath.sqrt(x)    
    
def Sqrt(x):
# Use our own version of the square root function 
# Negative arguments give complex values
    if x<0:
        return ComplexSqrt(x)
    else:
        return RealSqrt(x)

def HighSchool(a,b,c):
# High School version          NR eqn 5.6.2
    d = Discriminant(a,b,c)
    x1 = (-b + Sqrt(d))/(2*a)
    x2 = (-b - Sqrt(d))/(2*a)    
    return x1, x2
    
def Fagnano(a,b,c):
# Conte di Fagnano version     NR eqn 5.6.3
    d = Discriminant(a,b,c)
    x1 = 2*c/(-b - Sqrt(d))
    x2 = 2*c/(-b + Sqrt(d))
    return x1, x2
    
def Numerical(a,b,c):
# Numerically robust version   NR eqn 5.6.4 
# This is essentially the modified Fagnano formulae (4,5) described in Nievergelt. 
# Note that the x1 and x2 definitions are swapped with respect to NR 
# so as to correspond to the other methods.
    d = Discriminant(a,b,c)    
    q = -(b + Sign(b)*Sqrt(d))/2       
    x1 = c/q
    x2 = q/a
    return x1, x2
    
def NumericalAnalyst(a,b,c):
# Described as the numerical analysts' quadratic formulae (11, 12) in Nievergelt
# should be basically the same as the above.
    h = b/2
    d = h**2 - a*c
    v = h + Sign(b)*Sqrt(d)       
    x1 = -c/v
    x2 = -v/a
    return x1, x2    
    
def Sign(x):
# Seems like python doesn't have an intrinsic sign function. 
# Write our own with default value of 1 (also if x is zero).
    sign = 1
    if x<0:
        sign = -1
    return sign
