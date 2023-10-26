from scipy.integrate import fixed_quad
import numpy as np

def exact():
    Iexact = np.pi* ( (np.pi)**2 + (17.0/32.0))
    return Iexact

def integrand(x):
    integrand = x**2*(np.cos(x))**4
    return integrand
    
Integral = fixed_quad(integrand, 0.0, 2.0*np.pi, args=(), n=11)

print(Integral)
Iexact = exact()
print('Iexact',Iexact)
