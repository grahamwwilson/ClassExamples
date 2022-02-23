# mymodels.py
# Various simple model functions
# Add your own ...

import numpy as np

def linemodel(x, intercept, slope):  # simple straight line model with explicit parameters
    return intercept + slope*x

def quadmodel(x, a0, a1, a2):        # quadratic model with explicit parameters
    return a0 + a1*x + a2*x**2

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
