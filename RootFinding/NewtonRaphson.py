# NewtonRaphson.py
#
# Demo root finding with simple function, namely sin(x).
#
import math
import rfArgs
import myPythonCheck

def f(x):                                     # The function, f(x), whose zero we seek
    f = math.sin(x)
    return f
    
def fp(x):                                    # The first derivative of f(x)
    fp = math.cos(x)
    return fp
    
# Start of main program
myPythonCheck.Check()                         # Enforce use of python3

a,b,tol = rfArgs.getArguments(None)           # Read command line arguments 
rfArgs.showArgs(a,b,tol)                      # for bracketing interval (a,b) and tolerance |x - x_root|.

# Check the function is bracketed by [a,b]
xmin = a
xmax = b
fmin = f(xmin)
fmax = f(xmax)
fab = fmin*fmax

if fab < 0.0:
   print('Function is bracketed. [',xmin,',',xmax,']',fmin,fmax)
elif fab > 0.0:
   print('Function is not bracketed ... ',fmin,fmax)
else:
   print('One of the end-points likely is a root ...',fmin,fmax)   

# Let's implement Newton-Raphson method
# and check that the updated point is still within the interval
dx = xmax - xmin

niterations = 0
x = (xmin + xmax)/2.0
fx = f(x)
    
print('Initial bracket [',min(xmin,x,xmax),',',max(xmin,x,xmax),']',f(min(xmin,x,xmax)),f(max(xmin,x,xmax)))    

# Biggest hazard is likely that the correction overshoots the 
# existing bracketed interval. Choose a better initial bracketing interval
errorcode = 0
while abs(dx) > tol:
    print('Iteration ',niterations,' root estimate ',x,' with f = ',f(x),' dx = ',dx)   
    dx = - f(x)/fp(x)
# update the estimate
    x = x + dx
    fx = f(x)
    if x < xmin or x > xmax:             # check if still bracketed
        print("x value is now outside the initial bracket! will exit!",x)
        errorcode += 1
        break
    print('Bracket iteration',niterations,' [', min(xmin,x,xmax),',',max(xmin,x,xmax),']',x)  
    niterations +=1
    if niterations >= 100:
        print('Too many iterations .... will exit!') 
        errorcode += 2
        break        
            
if errorcode == 0:
    print( )           
    print('Final estimate, x=',x,' with error of',abs(dx),' with fn = ',f(x))
    print('Total number of iterations = ',niterations)
    print('deviation = estimate - true-value =',x - math.pi)
else:
    print( )
    print('Error occurred: errorcode ',errorcode)
