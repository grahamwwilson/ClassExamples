# pendulumODE.py
#
# Gather all the methods specific to this 
# particular ODE problem in this module
#
# Solve the initial-value problem ODE for a simple pendulum. 
# We keep the sin(theta) term rather than using 
# the sin(theta) = theta small angle approximation.
#
# Write as state-vector, y = (theta, omega)
# with two coupled first-order ordinary differential equations
#
#    dy0/dt = dtheta/dt = omega
#    dy1/dt = domega/dt = (-g/l) sin(theta)
#

import numpy as np
import sys
from scipy import special   # for scipy.special.ellipk special function 
# See https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.ellipk.html


def calcGradients(y, parameters):
#
# Evaluate RHS vector of gradients at time associated with the state vector, y
# where the components are y[0] = theta, y[1] = omega
#

    g = parameters[0]
    l = parameters[1]
    theta  = y[0]
    omega  = y[1]

    gradients = np.array( [ omega, (-g/l)*np.sin(theta) ])
    return gradients
    
def T0(parameters):
    g = parameters[0]
    l = parameters[1]
    w0sq = g/l
    T0 = 2.0*np.pi/np.sqrt(w0sq)
    return T0
 
def Texact(parameters,y0):
    g = parameters[0]
    l = parameters[1]
    theta0 = y0[0]                            # launch angle assuming initial value is launch
    w0sq = g/l
    T0 = 2.0*np.pi/np.sqrt(w0sq)
    
    k = np.sin(0.5*theta0)                    # k parameter - defined by the angular amplitude
# Calculate corresponding finite amplitude period using 
# the complete elliptic integral of the first kind of Legendre form
    m = k**2                                  # Conform with ellipk parametrization in terms of m
    period = T0*(2.0/np.pi)*special.ellipk(m) # Use formula (2) from p3 of 
                                              # Pendulum Experiment writeup (see HW4 link on web page)

    return period         

def Energy(y, parameters):
# Calculate mechanical energy E = K + U for simple pendulum. 
# Essentially this is E/m as the mass does not really need to be specified 
# but have set it to m=1 kg for definiteness.
    g = parameters[0]
    l = parameters[1]
    theta  = y[0]
    omega  = y[1]
    m = 1.0                  # Set m = 1.0 kg
    I = m*l**2               # Rotational inertia for point mass about pivot
    E = m*g*l*(1.0-np.cos(theta)) + 0.5*I*omega*omega
    return E
    
def PrintState(y, parameters, t, istep, E0, stateString = "End"):
    print()
    print(stateString,'state ',t,y)
    print(stateString,'time: ',t,'s  angle:',y[0],'rad')
    print(stateString,'angular speed is ',y[1],' rad/s ')
    print(stateString,'energy ratio ',Energy(y,parameters)/E0)
    print('t,istep',t,istep)

def PrintHeader(ofile):    
    print('#i  t[s]   theta [rad]       omega [rad/s]        Eratio ',file=ofile)
    
def PrintStep(y, parameters, t, istep, E0, ofile):
    print(istep, t, y[0], y[1], Energy(y,parameters)/E0, file=ofile)
    
def PrintHeaderError(ofile):    
    print('#i         t[s]            theta [rad]          omega [rad/s]          Ediff           d(theta)          d(omega) ',file=ofile)    
    
def PrintStepError(y, y1, y2, parameters, t, istep, E0, ofile):
#
# Note that the truncation error may indeed be a factor of 15 less than the 
# round-off error value of 2.2e-16 but 
# this implies that the calculation is dominated by round-off error.
#    eps = sys.float_info.epsilon
#
    print(istep, t, y[0], y[1], (Energy(y,parameters)/E0)-1.0, (y2[0]-y1[0])/15, (y2[1]-y1[1])/15, file=ofile)    
