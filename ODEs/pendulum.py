import numpy as np
import matplotlib.pyplot as plt
import myPythonCheck
import pendArgs
import stepper                  # ODE stepping algorithm
import pendulumODE as p         # ODE specific functions
#
# Solve the initial-value problem ODE for a simple pendulum
#
myPythonCheck.Check()                                                           # Enforce use of python3
theta, omega, g, l, dt, sMethod, tMax, ofname = pendArgs.getArguments(None)     # Read command line arguments 
pendArgs.showArgs(theta, omega, g, l, dt, sMethod, tMax, ofname)                # for pendulum ODE

ofile = open(ofname, "w")

y0 = np.array( [ theta, omega ])
y  = np.copy(y0)   # Set initial values

t = 0.0
parameters = [g, l]

E0 = p.Energy(y, parameters)       # Initial energy - hopefully this is conserved!
istep = 0
t = 0.0
yprev = y

# Write header and initial conditions to output file
p.PrintHeader(ofile)
p.PrintStep(y, parameters, t, istep, E0, ofile)

while t < tMax:
    yprev = y; tprev = t
# Calculate new position and velocity of projectile using chosen method
    y, t, istep = stepper.Stepper(y, dt, parameters, istep, sMethod)
    p.PrintStep(y, parameters, t, istep, E0, ofile)    

p.PrintState(y, parameters, t, istep, E0)

ofile.close()
