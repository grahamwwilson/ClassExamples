# CloseToPerfect.py
import random
import math
#
# Illustrate importance sampling for the integral(0,1) of cos(pi x/2). 
# We cheat here and use fp = (pi/2) cos(pi x / 2)
# (the prefactor is 1/integral - so only possible when we know what the answer is 
#  - which defeats the purpose ...)
#

SEED = 203
random.seed(SEED)       # Initialize random number generator using specified seed
NTRIES = 100        # Number of random numbers to generate
gsum = 0.0
ggsum = 0.0
N = 0                   # Keep track of number of accepted values for u

for i in range(NTRIES):
    u = random.uniform(0.0,1.0) # standard uniform random numbers in range [0.0,1.0)
# Use hit and miss to keep values of u that follow p(u) = (pi/2) cos(pi x / 2)
    ytest = 0.5*math.pi*random.uniform(0.0,1.0) 
    y = 0.5*math.pi*math.cos(0.5*math.pi*u)
    if (y > ytest):                  # u is thus in the acceptance region
        N +=1
        h = math.cos(0.5*math.pi*u)  # the original integrand
        fp = y                       # the sampling pdf
        g = h/fp                     # the new integrand to be sampled with -
        gsum += g                    # random variables from the fp distribution
        ggsum += g*g

# Calculate post-generation statistics
samplemeang = gsum/float(N)
samplemeangg = ggsum/float(N)
besselfactor = float(N)/float(N-1)
samplevariance = besselfactor*(samplemeangg - samplemeang*samplemeang)
samplesd = math.sqrt(max(0.0,samplevariance))

# Summary
print(' ')
print('Summary based on',N,'samples using SEED',SEED)
print('Observed mean ',samplemeang)
print('Observed rms and variance',samplesd, samplesd**2)
print('RESULT <g> = ',samplemeang,' +- ',samplesd/math.sqrt(N))
print('Acceptance efficiency ',N/NTRIES)
gmean = samplemeang
#dgmean = samplesd/math.sqrt(N)
diff = (gmean - (2.0/math.pi))
print('Correct result = ',2.0/math.pi)
print('Deviation = ',diff)

