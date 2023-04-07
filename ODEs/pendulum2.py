import numpy as np
import matplotlib.pyplot as plt
import myPythonCheck
import argparse
from stepper import Stepper     # ODE stepping algorithm
import pendulumODE as p         # ODE specific functions

def main(theta, omega, g, l, dt, sMethod, tMax, ofname):
#
# Solve the initial-value problem ODE for a simple pendulum
#
    ofile = open(ofname, "w")

    y0 = np.array( [ theta*np.pi/180.0, omega ])
    y  = np.copy(y0)   # Set initial values

    parameters = [g, l]

    E0 = p.Energy(y, parameters)       # Initial energy - hopefully this is conserved!
    istep = 0
    t = 0.0

# Write header and initial conditions to output file
    p.PrintHeader(ofile)
    p.PrintStep(y, parameters, t, istep, E0, ofile)

    while t < tMax:
# Calculate one time-step advanced theta and angular velocity 
# of pendulum using chosen method
        y, t, istep = Stepper(y, dt, parameters, istep, sMethod)
        p.PrintStep(y, parameters, t, istep, E0, ofile)    

    p.PrintState(y, parameters, t, istep, E0)

    ofile.close()

if __name__ == '__main__':

    myPythonCheck.Check()   #  Enforce use of python3

    parser = argparse.ArgumentParser(description="Pendulum Motion")
    parser.add_argument("-a", "--a",  type=float, default=45.0, help="Initial launch angle (degrees)")
    parser.add_argument("-w", "--w",  type=float, default=0.0,  help="Initial angular velocity (rad/s)")    
    parser.add_argument("-g", "--g",  type=float, default=9.80, help="Acceleration due to gravity (m/s^2)")
    parser.add_argument("-l", "--l",  type=float, default=1.2,  help="Pendulum length (m)")    
    parser.add_argument("-d", "--dt", type=float, default=0.01, help="Time-step (s)")
    parser.add_argument("-s", "--s",  type=int,   default=2,    help="Stepper method (0=Euler, 2=RK2)")
    parser.add_argument("-t", "--t",  type=float, default=20.0, help="Evolution duration (s)")     
    parser.add_argument("-f", "--f",  type=str,   default="pendulum.dat", help="Output file name")         
    
    args=parser.parse_args()
    print('Found argument list: ',args)
    
    main(args.a, args.w, args.g, args.l, args.dt, args.s, args.t, args.f)
