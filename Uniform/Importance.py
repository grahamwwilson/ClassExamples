# Importance.py
import random
import math
#
# Illustrate importance sampling for the integral(0,1) of cos(pi x/2). 
# Using fp = 1.5(1 - x^2) for the sampling distribution.
#

SEED = 203
random.seed(SEED)       # Initialize random number generator using specified seed
NTRIES = 1000000        # Number of random numbers to generate
gsum = 0.0
ggsum = 0.0
N = 0                   # Keep track of number of accepted values for u

for i in range(NTRIES):
    u = random.uniform(0.0,1.0) # standard uniform random numbers in range [0.0,1.0)
# Use hit and miss to keep values of u that follow p(u) = 1.5 (1 - u**2)
    ytest = 1.5*random.uniform(0.0,1.0) 
    y = 1.5*(1.0-u**2)
    if (y > ytest):                 # u is thus in the acceptance region
        N +=1
        h = math.cos(0.5*math.pi*u)  # the original integrand
        fp = 1.5*(1.0-u**2)          # the sampling pdf
        g = h/fp                     # the new integrand to be sampled with random variables from the fp distribution
        gsum += g
        ggsum += g*g

# Calculate post-generation statistics
samplemeang = gsum/float(N)
samplemeangg = ggsum/float(N)
besselfactor = float(N)/float(N-1)
samplevariance = besselfactor*(samplemeangg - samplemeang*samplemeang)
samplesd = math.sqrt(samplevariance)

# Summary
print(' ')
print('Summary based on',N,'samples using SEED',SEED)
print('Observed mean ',samplemeang)
print('Observed rms and variance',samplesd, samplesd**2)
print('RESULT <g> = ',samplemeang,' +- ',samplesd/math.sqrt(N))
print('Acceptance efficiency ',N/NTRIES)
gmean = samplemeang
dgmean = samplesd/math.sqrt(N)
z = (gmean - (2.0/math.pi))/dgmean
print('Correct result = ',2.0/math.pi)
print('Normalized deviation, z = ',z,' standard deviations')

