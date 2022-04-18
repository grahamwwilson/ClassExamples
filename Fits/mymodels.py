# mymodels.py
# Various simple model functions
# Add your own ...

import numpy as np

def linemodel(x, intercept, slope):  # simple straight line model with explicit parameters
    return intercept + slope*x

def quadmodel(x, a0, a1, a2):        # quadratic model with explicit parameters
    return a0 + a1*x + a2*x**2
    
def polynomial(x1, a0, a1, a2, a3, a4, a5, a6, a7, a8):        # polynomial with possibly too many parameters
    x = (x1 - 255.0)/200.0
    return a0 + a1*x + a2*x**2 + a3*x**3 + a4*x**4 + a5*x**5 + a6*x**6 + a7*x**7 + a8*x**8 
    
def polyexp(x1, a0, a1, a2, a3, a4, a5, a6, a7, a8, c, tauinv):        # polynomial with possibly too many parameters
    x = (x1 - 125.0)/100.0
    poly = a0 + a1*x + a2*x**2 + a3*x**3 + a4*x**4 + a5*x**5 + a6*x**6 + a7*x**7 + a8*x**8
    expo = c*np.exp(-(x1-125.0)*tauinv)
    return poly+expo
    
def rbw(x, bw, mz, gz, a0, a1, a2):
# rbwzz was "(x[0]*x[0]/( (x[0]*x[0] - x[1]*x[1])*(x[0]*x[0] - x[1]*x[1]) + x[1]*x[1]*x[2]*x[2] ))"
# So    (m**2/ [ (m**2 - m0**2)**2 + (m0*g)**2 ]
# ie   s/ [ (s - m**2)**2 + (G m)**2
    s = x**2
    rbwigner = bw*s/ ( (s - mz**2)**2 + (mz*gz)**2 )
    z = (x-125.0)/100.0
    return rbwigner + a0 + a1*z + a2*z**2        

def exponential(x, c, tau):          # exponential model
    return c*np.exp(-x/tau)

def srcurve(x, x0, sigx, yamplitude, yoffset):     # cdf of Gaussian for rising S-curve from chopper-wheel
    z = (x-x0)/sigx
    phix = 0.5*(1.0 + np.erf(z/np.sqrt(2.0)))
    yvalue = yoffset + yamplitude*phix
    return yvalue

def sfcurve(x, x0, sigx, yamplitude, yoffset):     # cdf of Gaussian for falling S-curve from chopper-wheel
    z = (x-x0)/sigx
    phix = 0.5*(1.0 - np.erf(z/np.sqrt(2.0)))
    yvalue = yoffset + yamplitude*phix
    return yvalue
