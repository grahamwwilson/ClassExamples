import math

def f(x):
    f = x**2*(math.cos(x))**4
    return f

Iexact = math.pi* ( (math.pi)**2 + (17.0/32.0))
print(Iexact)

a = 0.0
b = 2.0*math.pi

N = 1000

# Implement N Riemann sums evaluated at mid-point of each strip.
dx = (b-a)/N
Isum = 0.0
for i in range(N):
    xi = a + dx*i + 0.5*dx
    print(i, xi, f(xi))
    Isum += f(xi)
Isum = Isum*dx    

print('middle Riemann sum method') 
print('Isum                 = ',Isum)
print('Iexact               = ',Iexact)
print('Deviation            = ',Isum-Iexact)
print('fractional deviation = ',(Isum-Iexact)/Iexact)
