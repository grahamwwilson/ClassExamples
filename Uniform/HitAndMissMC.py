# HitAndMissMC.py
import random
import math
#
# Illustrate hit and miss MC integration for the integral(0,1) of cos(pi x/2). 
# Sample just from the uniform distribution on (0,1).
#

SEED = 205
random.seed(SEED)       # Initialize random number generator using specified seed
N = 1000000             # Number of random numbers to generate
gsum = 0.0
ggsum = 0.0

Area = 1.0*1.0          # Sampled area in the (x, f(x) box)
# So since the area is 1 we don't need to do any normalization

for i in range(N):
    u = random.uniform(0.0,1.0)  # standard uniform random numbers in range [0.0,1.0)
    ytest = 1.0*random.uniform(0.0,1.0) 
    y = math.cos(0.5*math.pi*u) 
    if ytest < y:                  # Increment sums
       gsum += 1.0              
       ggsum += 1.0*1.0
    else:                          # We don't need this else statement but it makes it explicit
       gsum += 0.0                 # that we do have N observations of either 0 or 1.
       ggsum += 0.0*0.0              

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
gmean = samplemeang
dgmean = samplesd/math.sqrt(N)
z = (gmean - (2.0/math.pi))/dgmean
print('Correct result = ',2.0/math.pi)
print('Normalized deviation, z = ',z,' standard deviations')
