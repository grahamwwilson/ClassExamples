# BisectionExample.py
#
# Demo root finding with simple function, namely sin(x).
#
import math
import rfArgs
import myPythonCheck

def f(x):                                     # The function, f(x), whose zero we seek
    f = math.sin(x)
    return f
        
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

errorcode = 0

if fab < 0.0:
   print('Function zero is bracketed. Yay !',fmin,fmax)
elif fab > 0.0:
   print('Function zero is not bracketed. Are you sure there should be a root here?',fmin,fmax)
   errorcode += 1
else:
   print('One of the end-points likely is a root ...',fmin,fmax)
   errorcode += 2

# let's try bi-section
dx = xmax - xmin

niterations = 0

while (errorcode == 0 and abs(dx) > tol):
    fmin = f(xmin)
    fmax = f(xmax)
    xmid = (xmin+xmax)/2.0
    fmid = f(xmid)
    
    if (fmin > 0.0 and fmid < 0.0) or (fmin < 0.0 and fmid > 0.0):
# update bracket to [xmin, xmid] 
       xmax = xmid
       dx = xmax - xmin
    elif (fmax > 0.0 and fmid < 0.0) or (fmax < 0.0 and fmid > 0.0):
# update bracket to [xmid, xmax]    
       xmin = xmid
       dx = xmax - xmin
    else:
       print('Should not get here ?? ',xmin,xmid,xmax,fmin,fmid,fmax)
       
    niterations += 1
    print('Iteration ',niterations,'Updated bracketing interval  ',xmin,xmax,' of length ',dx)
    if niterations >= 100:
       print('Too many iterations - need to run again with looser tolerance requirement - will exit')
       errorcode += 4
       break
        
if errorcode == 0:        
    xmid = (xmin+xmax)/2.0
    print()
    print('Final bracketing interval ',xmin,xmax,' of length ',dx,' with x:',xmid,'f(x):',f(xmid))
    print('Total number of iterations = ',niterations)
    print('deviation = estimate - true-value =',xmid - math.pi)    
else:
    print()
    print('Error occurred: errorcode ',errorcode)
