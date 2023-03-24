# mymodels.py
# Various simple model functions
# Add your own ...

import numpy as np
import math

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
    
def wardyang(E):
    c1 = 0.3224
    c2 = 1.242e-4
    c3 = -1.446e-2
    fE = (c1/np.sqrt(E)) + c2*E + c3
    sigma = E*fE
    fres = sigma/E
    return 100.0*fres
    
def deltaM(x, msmu):
#    print(x)
#    print(msmu)
    mW=80.415
    mmu=0.1056
    beta = np.arctan(x)
#    print(beta)
    msnusq = msmu**2 - mmu**2 + mW**2*np.cos(2.0*beta)
    dm = msmu-np.sqrt(msnusq)
# Asymptote
    Msnusq = msmu**2 - mmu**2 - mW**2
    print('Asymptotic Msnu = ',np.sqrt(Msnusq))    
    return dm
    
def sspdf(x, m1, m2):
# Dilepton mass distribution for same-sign eigenvalues
    mz = 91.1876
    sumofsq = m1**2 + m2**2
    diffsq = m2**2 - m1**2
    top = pow(x,4.0) - 2.0*sumofsq*x*x + diffsq**2
    bot = (x**2 - mz**2)**2
    other = -2.0*x**4 + (3.0*sumofsq + 2.0*m1*m2)*x*x + diffsq**2
    value = 1.0e-7*x*np.sqrt(top)*other/bot
    return value
    
def ospdf(x, m1, m2):
# Dilepton mass distribution for opposite-sign eigenvalues
    mz = 91.1876
    sumofsq = m1**2 + m2**2
    diffsq = m2**2 - m1**2
    top = pow(x,4.0) - 2.0*sumofsq*x*x + diffsq**2
    bot = (x**2 - mz**2)**2
    other = -2.0*x**4 + (3.0*sumofsq - 2.0*m1*m2)*x*x + diffsq**2
    value = 0.18e-7*x*np.sqrt(top)*other/bot
    return value 
    
def mumu(x):
    """ Di-muon point cross-section in nb vs center-of-mass energy in GeV """
    M = 0.1056583755
    E = 0.5*x
    betasq = 1.0 - (M/E)**2
    beta = np.sqrt(betasq)
    cross = 86.8*beta*0.5*(3.0-beta**2)/(4.0*E**2) 
    return cross 
