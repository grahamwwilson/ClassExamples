#
# Solve pendulum differential equation numerically. Here the ODE includes 
# the exact sin(theta) term (no small angle approximation) and the 
# ODE has been rewritten using the free boundary problem approach.
#
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp   # ODE initial value problem solver
from scipy.optimize import newton       # Newton-Raphson zero (or root) finding
from scipy import special
import argparse
from myUtils import PrintSoln2

# The initial coupled ODEs are:
# dtheta/dt = omega, domega/dt = -(g/l)*sin(theta).
#
# We use the free-boundary problem approach to rewrite the problem as 
# dtheta/dz = omega*Tint, domega/dz = -(g/l)*Tint*sin(theta), dTint/dz = 0
# where t = z Tint with z in [0,1].
#
# The specific problem with specified initial conditions for (theta, omega) at z=0.0,  
# but theta=0.0 at z = 1.0, amounts to iteratively finding the zero 
# of fzero (namely Tint), which adaptively advances the differential equation 
# to z = 1.0 for various trial values of Tint.
#

def f(z, y, params):
    """
      Calculate the gradients of the differential equation
    """
    theta, omega, Tint = y                   # unpack current values of y
    g, l = params                            # unpack parameters
    w0sq = g/l
    derivs = [omega*Tint, -w0sq*Tint*np.sin(theta), 0.0]
    return derivs
    
def fzero(Tint):
    """
      Function whose zero corresponds to the desired integration time, Tint.
    """
    zStart = 0.0
    zStop =  1.0
    times = np.linspace(zStart,zStop,101)
    z_span = [zStart, zStop]
    # Bundle parameters and initial conditions for ODE solver
    params = [G, L]                        # parameters
    y0 = [theta0, omega0, Tint]            # initial conditions
    soln = solve_ivp(f, z_span, y0, rtol=100*EPS, atol=1.0e-16, dense_output=True, t_eval=times, method='DOP853', args=(params,))
    z    = soln.t
    q, w, T = soln.y    
    return q[100]         # theta value at end-point
    
EPS = np.finfo(float).eps                    # machine precision - around 2.2e-16

parser = argparse.ArgumentParser(description='Pendulum Timer Simulator with ODE')
parser.add_argument("-q", "--theta0", type=float, default=math.pi/3, help="Initial angle (rad)")

args=parser.parse_args()
print('Found argument list: ')
print(args)
theta0=args.theta0      # Initial angle (rad)

oscillationsfile = open("Oscillations.dat", "w")
print('# i       time[s]       theta[rad]      omega[rad/s]      ',
      ' Energy[%]       theta_0[rad]        omega_0[rad/s]       ',
      'drag-induced angular acceleration  [rad/s^2]',
      file=oscillationsfile)  # File header

# Parameters
G = 9.80      # acceleration due to gravity [m/s^2]
L = 1.5       # pendulum length
    
omega0 = 0.0       # initial angular velocity [rad/s]
EoverM0 = G*L*(1.0 - np.cos(theta0))  # Initial value of E/m
w0sq = G/L                    # pendulum angular frequency squared [rad^2/s^2]
wmaxsq = 2.0*w0sq*(1.0-math.cos(theta0))  # max angular velocity squared assuming no drag

print('Defined parameters ',G,L,theta0,wmaxsq)

# Derived quantities.
w0 = np.sqrt(w0sq)
T0 = (2.0*np.pi/w0)
k = np.sin(0.5*theta0)
Texact = T0*(2.0/np.pi)*special.ellipk(k*k) # Estimate of the initial period
Tint = Texact/4.0
print('Derived quantities: w0sq, T0, w0, Texact, Tint',w0sq,T0,w0,Texact,Tint)

Tguess = 1.01*Texact/4.0
print('Tguess : ',Tguess)

# Bundle parameters and initial conditions for ODE solver
params = [G, L]             # parameters

# Find the quarter-period corresponding to the theta value passing through zero 
# using a scipy root-finding algorithm  (scipy.optimize.newton)
# Here we basically adjust the integration time of the ODE until theta(Tint) = 0.0 rad
# (ie. until the pendulum has fallen to the vertical position).

Tfound = newton(fzero, Tguess-0.05, tol=EPS, x1=Tguess+0.1)  # Find zero

# Repeat the ODE evaluation using this value of the quarter period reporting 101 values of the trajectory parameters.
print('Tfound = ',Tfound,type(Tfound))
y0 = [theta0, omega0, Tfound]
zStart = 0.0
zStop =  1.0
times = np.linspace(zStart,zStop,101)
z_span = [zStart, zStop]
soln = solve_ivp(f, z_span, y0, rtol=100*EPS, atol=1.0e-16, dense_output=False, t_eval=times, method='DOP853', args=(params,))

PrintSoln2(soln)

print("Fractional error: ",(Tfound-(Texact/4.0))/(Texact/4.0))   
