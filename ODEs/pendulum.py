import numpy as np
import matplotlib.pyplot as plt
import myPythonCheck
import argparse
from stepper import Stepper     # ODE stepping algorithm
import pendulumODE as p         # ODE specific functions

def main(y0, parameters, dt, tMax, sMethod, ofname):
    """ Solve the initial-value ODE problem for a simple pendulum using various 
        fixed step-size stepping algorithms 
        
        y0:         Initial values array (theta0, omega0)
        parameters: Parameters list (g, l)
        dt:         Time-step in seconds
        tMax:       Evolve ODE until time tMax (in seconds)
        sMethod:    Stepper method
        ofname:     Output file name               """
        
    ofile = open(ofname, "w")
    E0 = p.Energy(y0, parameters)      # Initial energy - hopefully this is conserved and does not change.    
    y  = np.copy(y0)                   # Copy initial values to initial "state-vector' 

    istep = 0
    t = 0.0
# Write header and initial conditions to output file
    p.PrintHeader(ofile)
    p.PrintStep(y, parameters, t, istep, E0, ofile)

    while t < tMax:
# Calculate one time-step advanced theta and angular velocity 
# of pendulum using chosen method while total elapsed time does not exceed tMax
        y, t, istep = Stepper(y, dt, parameters, istep, sMethod)
        p.PrintStep(y, parameters, t, istep, E0, ofile)    

    p.PrintState(y, parameters, t, istep, E0)
    ofile.close()

if __name__ == '__main__':

    myPythonCheck.Check()   #  Enforce use of python3

    parser = argparse.ArgumentParser(description="Pendulum Motion")
    parser.add_argument("-a", "--a",  type=float, default=np.pi/4.0, help="Initial launch angle (rad)")
    parser.add_argument("-w", "--w",  type=float, default=0.0,  help="Initial angular velocity (rad/s)")    
    parser.add_argument("-g", "--g",  type=float, default=9.80, help="Acceleration due to gravity (m/s^2)")
    parser.add_argument("-l", "--l",  type=float, default=1.2,  help="Pendulum length (m)")    
    parser.add_argument("-d", "--dt", type=float, default=0.01, help="Time-step (s)")
    parser.add_argument("-t", "--t",  type=float, default=20.0, help="Evolution duration (s)")
    parser.add_argument("-s", "--s",  type=int,   default=2,    help="Stepper method (0=Euler, 2=RK2)")         
    parser.add_argument("-f", "--f",  type=str,   default="pendulum.dat", help="Output file name")         
    
    args=parser.parse_args()
    print('Found argument list: ',args)
    
    y0 = np.array( [ args.a, args.w ])   # The initial values for (theta, omega)
    parameters = [args.g, args.l]        # The problem parameters (g, l)
    
    main(y0, parameters, args.dt, args.t, args.s, args.f)
