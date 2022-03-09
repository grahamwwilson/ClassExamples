# myStepper.py
import math
import numpy as np

# Steppers are written with notation as in Numerical Recipes
# To implement RK4 should be straightforward for you  
# to take RK2 and implement RK4
# (EulerP and RK2P below are provided because they are arguably 
#  more understandable - but a little harder to extend - feel free to ignore).

def calcGradients(y, parameters):
#
# Evaluate RHS vector of gradients at time associated with the state vector, y
# where the components are y[0] = theta, y[1] = omega
#

    g = parameters[0]
    l = parameters[1]
    theta  = y[0]
    omega  = y[1]

    gradients = np.array( [ omega, (-g/l)*math.sin(theta) ])
    return gradients
    
def Euler(y, dt, parameters, istep):
# Numerical Recipes Equation 17.1.1
     
    t = istep*dt
    print('Pre-step:  ',t,istep,'y = ',y)
    
    grad1 = calcGradients(y, parameters)    
    k1 = grad1*dt

    y = y + k1                                    # Euler update 
    
    istep += 1
    t = istep*dt
    
    print('Post-step: ',t,istep,'y = ',y)    
    return y, t, istep
    
def RK2(y, dt, parameters, istep):
# Numerical Recipes Equation 17.1.2
# Rewrite RK2 with same notation as RK4
     
    t = istep*dt
    print('Pre-step:  ',t,istep,'y = ',y)

    grad1 = calcGradients(y, parameters)
    k1 = grad1*dt
    
    y2 = y + 0.5*k1                               # Half-step evolution
    grad2 = calcGradients(y2, parameters)
    k2 = grad2*dt
    
    y = y + k2                                    # Full-step evolution using mid-point gradient
        
    istep += 1
    t = istep*dt
    
    print('Post-step: ',t,istep,'y = ',y)    
    return y, t, istep            
      
def EulerP(y, dt, parameters, istep):
# Numerical Recipes Equation 17.1.1
     
    t = istep*dt
    print('Pre-step:  ',t,istep,'y = ',y)
    
    gradients = calcGradients(y, parameters)    
    y = y + gradients*dt
    
    istep += 1
    t = istep*dt
    
    print('Post-step: ',t,istep,'y = ',y)    
    return y, t, istep
    
def RK2P(y, dt, parameters, istep):
# Numerical Recipes Equation 17.1.2
     
    t = istep*dt
    print('Pre-step:  ',t,istep,'y = ',y)

    gradients = calcGradients(y, parameters)
    yp = y + gradients*0.5*dt                     # Half-step evolution

    gradientsp = calcGradients(yp, parameters)
    y = y + gradientsp*dt                         # Full-step evolution using mid-point gradient
        
    istep += 1
    t = istep*dt
    
    print('Post-step: ',t,istep,'y = ',y)    
    return y, t, istep
    
def Stepper(y, dt, parameters, istep, stepperMethod):

    if stepperMethod == 0:
        y, t, istep = Euler(y, dt, parameters, istep)
        return y, t, istep
    elif  stepperMethod == 2:
        y, t, istep = RK2(y, dt, parameters, istep)
        return y, t, istep        
