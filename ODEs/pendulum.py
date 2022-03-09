import numpy as np
import matplotlib.pyplot as plt
import myPythonCheck
import pendArgs
import math
import myStepper

def Energy(y, parameters):
    g = parameters[0]
    l = parameters[1]
    theta  = y[0]
    omega  = y[1]
    m = 1.0                  # Set m = 1.0 kg
    I = m*l**2           # Rotational inertia for point mass
    E = m*g*l*(1.0-math.cos(theta)) + 0.5*I*omega*omega
    return E

myPythonCheck.Check()                                             # Enforce use of python3
angle, omega, g, l, dt, sMethod = pendArgs.getArguments(None)     # Read command line arguments 
pendArgs.showArgs(angle, omega, g, l, dt, sMethod)                # for pendulum ODE

# Write as state-vector, y = (theta, omega)
# With two coupled ordinary differential equations
#  dy0/dt = dtheta/dt = omega
#  dy1/dt = domega/dt = (-g/l) sin(theta)

y0 = np.array( [ angle, omega ])
y  = np.copy(y0)   # Set initial values

t = 0.0
parameters = [g, l]

E0 = Energy(y, parameters)

istep = 0
t = 0.0
yprev = y
while t <= 20.0:
    yprev = y; tprev = t
# Calculate new position and velocity of projectile using chosen method
    y, t, istep = myStepper.Stepper(y, dt, parameters, istep, sMethod)
#    print(istep,Energy(y,parameters))

print()
print('Pre-end state  ',tprev, yprev)
print('Pre-end time:  ',tprev,'s  angle:',yprev[0],'rad')
print('Pre-end speed is  ',yprev[1],' rad/s ')
print('Pre-end energy ratio ',Energy(yprev,parameters)/E0)

print()
print('Post-end state ',t,y)
print('Post-end time: ',t,'s  angle:',y[0],'rad')
print('Post-end speed is ',y[1],' rad/s ')
print('Post-end energy ratio ',Energy(y,parameters)/E0)
print('t,istep',t,istep)
