# ImportancePrime.py
import random
import math
#
# Illustrate importance sampling for the integral(0,1) of cos(pi x/2). 
# Using fp = C ( 1 - (pi^2 x^2)/8 + (pi^4*x^4)/384 ) for the sampling distribution.
#

SEED = 203
random.seed(SEED)       # Initialize random number generator using specified seed
NTRIES = 1000000        # Number of random numbers to generate
gsum = 0.0
ggsum = 0.0
N = 0                   # Keep track of number of accepted values for u

# Normalization constant such that int(0,1)fp(x) dx = 1
C = 1.0/(1.0 - (1.0/24.0)*math.pi**2 + (1.0/1920.0)*math.pi**4)
print('C = ',C)

for i in range(NTRIES):
    u = random.uniform(0.0,1.0) # standard uniform random numbers in range [0.0,1.0)
# Use hit and miss to keep values of u that follow p(u) = 1.5 (1 - u**2)
    ytest = C*random.uniform(0.0,1.0) 
    y = C*(1.0 - (math.pi**2)/8.0*u**2 + (math.pi**4)/384.0*u**4 )
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

