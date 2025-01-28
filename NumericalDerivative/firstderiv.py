#
# Demonstrate numerical first derivatives
#
import math
import argparse
import myPythonCheck

# Use a global variable to have both the sine function and polynomial 
# implementation easily switchable
which = 0

def f(x):

    val = 0.0
    if which==0:
        val = math.sin(x)
    if which==1:
        val = x**6    
    return val
    
def ForwardNaive(x0,h):

    x1 = x0 + h
#    h = x1 - x0
    
    fprime = (f(x1) - f(x0))/h

    return fprime    
    
def Forward(x0,h):

    x1 = x0 + h
#Numerical analyst's trick    
    h = x1 - x0
    
    fprime = (f(x1) - f(x0))/h

    return fprime 

def Backward(x0,h):
    xm1 = x0 - h
    h = x0 - xm1
    
    fprime = (f(x0) - f(xm1))/h
    
    return fprime 

def Centered(x0,h):

    x1 = x0 + h
    xm1 = x0 - h
    twoh = x1 - xm1
    
    fprime = (f(x1) - f(xm1))/twoh

    return fprime
    
def FourthOrder(x0,h):

    x1 = x0 + h
    xm1 = x0 - h
    twoh = x1 - xm1    
    xm2 = x0 - twoh
    x2 = x0 + twoh

    fprime = ( f(xm2) - f(x2) + 8.0*(f(x1) - f(xm1)) )/(6.0*twoh)
    
    return fprime
    
def MyPrint(algorithm,fprime,x0):
    # calculate correct value
    truefprime = 0.0
    if which==0: 
        truefprime = math.cos(x0)
    if which==1:
        truefprime = 6.0*x0**5
    print("algorithm: ", algorithm, "fprime = ",fprime,"true fprime = ",truefprime,"deviation = ",fprime - truefprime)
    
def main(algorithm, h, x0):    
    
#    x0 = math.pi/3.0

    print('which set to ',which)
    if which==0:
        print("Using f(x) = sin(x)")
    if which==1:
        print("Using f(x) = x**6")
    
    if algorithm==-1:
        fprime = ForwardNaive(x0,h)
        MyPrint(algorithm,fprime,x0)    
    
    if algorithm==0:
        fprime = Forward(x0,h)
        MyPrint(algorithm,fprime,x0)
        
    if algorithm==1:
        fprime = Backward(x0,h)
        MyPrint(algorithm,fprime,x0)
        
    if algorithm==2:
        fprime = Centered(x0,h)
        MyPrint(algorithm,fprime,x0) 
        
    if algorithm==3:
        fprime = FourthOrder(x0,h)
        MyPrint(algorithm,fprime,x0)                                
    
if __name__ == '__main__':

    myPythonCheck.Check()   #  Enforce use of python3

    parser = argparse.ArgumentParser(description="Numerical First Derivative")
    
    parser.add_argument("-w", "--w",  type=int,   default=0, help="Function 0=sin(x), 1=x**6")
    parser.add_argument("-a", "--a",  type=int,   default=0,    help="Algorithm method (-1=Naive, 0=FD, 1=BD, 2=CD, 3=FO") 
    parser.add_argument("-s", "--s",  type=float, default=0.1,  help="Step size")
    parser.add_argument("-x", "--x",  type=float, default=1.0, help="x-value ")
    
    args=parser.parse_args()
    print('Found argument list: ',args)    
    
    which = args.w
    
    main(args.a, args.s, args.x)   
