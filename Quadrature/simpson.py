# Use Simpson's rule to numerically integrate the HW2 P1 
# definite integral over [a,b] = [0, 2pi].
# For N=2, the formula is (dx/3) (f0 + 4f1 + 2f2 + 4f3 +f4)
import math
import myPythonCheck
import quadsArgs

def f(x):
    f = x**2*(math.cos(x))**4
    return f

myPythonCheck.Check()                          # Enforce use of python3
N,a,b = quadsArgs.getArguments(None)           # Read command line arguments 
quadsArgs.showArgs(N,a,b)                      # for numerical integration

Iexact = math.pi* ( (math.pi)**2 + (17.0/32.0))
print('Exact value of integral = ',Iexact)

# Implement extended Simpson's rule using 2N+1 function evaluations
dx = (b-a)/(2*N)
Isum = 0.0
for i in range(2*N+1):
    xi = a + dx*i
#    print(i, xi, f(xi))
    if (i==0 or i==2*N):       # endpoints
        Isum += f(xi)
    elif i%2==1:               # interior points of first type
        Isum += 4*f(xi)
    else:                      # interior points of second type
        Isum += 2*f(xi)    

Isum = Isum*dx/3       
       
print('Simpsons rule method')
print('Isum                 = ',Isum)
print('Iexact               = ',Iexact)
print('Deviation            = ',Isum-Iexact)
print('fractional deviation = ',(Isum-Iexact)/Iexact)
