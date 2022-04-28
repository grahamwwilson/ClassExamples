# quadraticMethods.py

# See "How (Not) to Solve Quadratic Equations", Yves Nievergelt, 
# The College Mathematics Journal, 34 (2003) 90-104.
# Available at https://www.jstor.org/stable/3595780
#
# Graham W. Wilson, 28-APR-2022

import math

def Discriminant(a,b,c):
    d = b**2 - 4*a*c
    return d

def HighSchool(a,b,c):
# High School version          NR eqn 5.6.2
    d = Discriminant(a,b,c)
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)    
    return x1, x2
    
def Fagnano(a,b,c):
# Conte di Fagnano version     NR eqn 5.6.3
    d = Discriminant(a,b,c)    
    x1 = 2*c/(-b - math.sqrt(d))
    x2 = 2*c/(-b + math.sqrt(d))
    return x1, x2
    
def Numerical(a,b,c):
# Numerically robust version   NR eqn 5.6.4. 
# This is essentially the modified Fagnano formulae (4,5) described in Nievergelt. 
# Note that the x1 and x2 definitions are swapped with respect to NR 
# so as to correspond to the other methods.
    d = Discriminant(a,b,c)    
    q = -(b + sign(b)*math.sqrt(d))/2       
    x1 = c/q
    x2 = q/a
    return x1, x2
    
def sign(x):
# Seems like python doesn't have an intrinsic sign function. Write our own.
    sign = 1
    if x<0:
        sign = -1
    elif x==0:
        sign = 0
    return sign
