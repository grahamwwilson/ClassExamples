import math
import myPythonCheck
import quadArgs

def f(x):
    f = x**2*(math.cos(x))**4
    return f

myPythonCheck.Check()                         # Enforce use of python3
N,a,b = quadArgs.getArguments(None)           # Read command line arguments 
quadArgs.showArgs(N,a,b)                      # for numerical integration

Iexact = math.pi* ( (math.pi)**2 + (17.0/32.0))
print(Iexact)

# Implement extended trapezoid rule
dx = (b-a)/N
Isum = 0.0
for i in range(N+1):
    xi = a + dx*i
#    print(i, xi, f(xi))
    if i==0 or i==N:
       Isum += 0.5*f(xi)
    else:
       Isum += f(xi)
       
Isum = Isum*dx       
       
print('Trapezoid rule method')
print('Isum                 = ',Isum)
print('Iexact               = ',Iexact)
print('Deviation            = ',Isum-Iexact)
print('fractional deviation = ',(Isum-Iexact)/Iexact)
