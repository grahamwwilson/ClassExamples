# myUtils.py
import numpy as np
import math

def PrintSoln(soln):
    t    = soln.t
    q, w = soln.y
    nrows = t.size
    tprev = 0.0
    for i in range(nrows):
        tvalue = t[i]
        theta = q[i]
        omega = w[i]
        print('Time step ',i,'t= ',tvalue,'dt=',tvalue-tprev,' theta = ',theta,' omega = ',omega)
        tprev = tvalue
        
def PrintSoln2(soln):
    z    = soln.t
    q, w, T = soln.y
    nrows = z.size
    tprev = 0.0
    
    for i in range(nrows):
        There = T[i]
        tvalue = z[i]
        theta = q[i]
        omega = w[i]
        
        print('Time step ',i,'T = ',There,'z= ',tvalue,'dz=',tvalue-tprev,' theta = ',theta,' omega = ',omega)
        tprev = tvalue        
