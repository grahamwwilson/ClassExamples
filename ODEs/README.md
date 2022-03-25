# ClassExamples/ODEs
Simple example for implementing ODEs

## pendulum.py

Simple Pendulum ODE

Do python3 pendulum.py -h to see command line arguments.

With default arguments, writes an output file called pendulum.dat 
that can be used for example for plots.

## pendulumODE.py
Module with functions used in both pendulum.py and stepper.py for 
this specific ODE problem. Functions include 
calcGradients, T0, Texact, Energy, PrintState, PrintHeader, PrintStep, 
PrintHeaderError, PrintStepError

## pendArgs.py
Used for passing arguments

## stepper.py
Generic stepping algorithms. 
You should code up RK4 yourself. You could also add error estimates 
and adaptive step-size control.
These can be applied (YMMV) to any ODE by providing 
a suitable calcGradients function to evaluate the RHS of the ODE system.
It is currently configured to use pendulumODE.calcGradients.

## plot.py
python3 plot.py

Plots some of the data from pendulum.dat using matplotlib
