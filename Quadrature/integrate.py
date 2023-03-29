from scipy.integrate import quad
import math

def exact():
    Iexact = math.pi* ( (math.pi)**2 + (17.0/32.0))
    return Iexact

def integrand(x):
    integrand = x**2*(math.cos(x))**4
    return integrand
    
Integral = quad(integrand, 0.0, 2.0*math.pi, epsabs=4.0e-13, limit=100)

print(Integral)
Iexact = exact()
print('Iexact',Iexact)
