#
# Demonstrate numerical first derivatives
#
import math
import argparse
import myPythonCheck

def f(x):
    return math.sin(x)
    
def Forward(x0,h):

    x1 = x0 + h
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
    
def MyPrint(algorithm,fprime):
    print("algorithm: ", algorithm, "fprime = ",fprime,"deviation = ",fprime-0.5)
    
def main(algorithm, h):    
    
    x0 = math.pi/3.0
    
    if algorithm==0:
        fprime = Forward(x0,h)
        MyPrint(algorithm,fprime)
        
    if algorithm==1:
        fprime = Backward(x0,h)
        MyPrint(algorithm,fprime)
        
    if algorithm==2:
        fprime = Centered(x0,h)
        MyPrint(algorithm,fprime) 
        
    if algorithm==3:
        fprime = FourthOrder(x0,h)
        MyPrint(algorithm,fprime)                                
    
if __name__ == '__main__':

    myPythonCheck.Check()   #  Enforce use of python3

    parser = argparse.ArgumentParser(description="Numerical First Derivative")
    parser.add_argument("-a", "--a",  type=int,   default=0,    help="Algorithm method (0=FD, 1=BD, 2=CD, 3=FO") 
    parser.add_argument("-s", "--s",  type=float, default=0.1,  help="Step size")
    
    args=parser.parse_args()
    print('Found argument list: ',args)    
    
    main(args.a, args.s)   
