# Pie.py
import random
import math

# Generate random points in a square of side-length 2 centered on (0,0) 
# and count number of points within 1 of the center.

SEED = 205
random.seed(SEED)
NINSTANCES = 4000000       # Number of random numbers to generate
NPRINT = 10

print('SEED set to ',SEED)
print('NINSTANCES set to ',NINSTANCES)

count = 0

# Generate uniform random numbers
for i in range(NINSTANCES):
# Generate x, y ~ Un(-1,1)
    x = 2.0*random.random() - 1.0 
    y = 2.0*random.random() - 1.0
    r = math.sqrt(x**2 + y**2)
    if i<NPRINT:
        print('trial',i,'x =',x,'y = ',y,'r = ',r)
    if r<=1.0:
        count+=1
    
print('Overall count = ',count)
f=float(count)/float(NINSTANCES)
print('Success fraction = ',f)
mypi = 4.0*f
print('Estimate of pi = ',mypi)
pcdeviation = 100.0*(mypi - math.pi)/math.pi
print('This deviates from ',math.pi,' by ',pcdeviation,'%')
