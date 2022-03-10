import numpy as np
import matplotlib.pyplot as plt
import myPythonCheck
import pendArgs
import math
import myStepper

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
    E = m*g*l*(1.0-math.cos(theta)) + 0.5*I*omega*omega
    return E

myPythonCheck.Check()                                                     # Enforce use of python3
theta, omega, g, l, dt, sMethod, tMax, ofname = pendArgs.getArguments(None)     # Read command line arguments 
pendArgs.showArgs(theta, omega, g, l, dt, sMethod, tMax, ofname)                # for pendulum ODE

ofile = open(ofname, "w")

y0 = np.array( [ theta, omega ])
y  = np.copy(y0)   # Set initial values

t = 0.0
parameters = [g, l]

E0 = Energy(y, parameters)       # Initial energy - hopefully this is conserved!
istep = 0
t = 0.0
yprev = y

# Write header and initial conditions to output file
print('#i  t[s]   theta [rad]       omega [rad/s]        Eratio ',file=ofile)
print(istep, t, y[0], y[1], Energy(y,parameters)/E0, file=ofile)

while t < tMax:
    yprev = y; tprev = t
# Calculate new position and velocity of projectile using chosen method
    y, t, istep = myStepper.Stepper(y, dt, parameters, istep, sMethod)
    print(istep, t, y[0], y[1], Energy(y,parameters)/E0, file=ofile)    

print()
print('End state ',t,y)
print('End time: ',t,'s  angle:',y[0],'rad')
print('End angular speed is ',y[1],' rad/s ')
print('End energy ratio ',Energy(y,parameters)/E0)
print('t,istep',t,istep)

ofile.close()

