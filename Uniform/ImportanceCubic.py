# ImportanceCubic.py
import random
import math
from MyKSTest import runKSTest
from Summary import summary

# Illustrate importance sampling for the integral(0,1) of cos(pi x/2). 
# Using fp = 1.5(1 - x^2) for the sampling distribution.
# In this case we apply a recipe for sampling, by using the inverse CDF method.
# This results in a cubic equation with 3 real roots. 
# Some analysis shows that only one (x_3) is in the physically appropriate (0,1) interval though.
# We also include a KS test to check that the sampled distribution is as expected.

SEED = 202
random.seed(SEED)       # Initialize random number generator using specified seed
NTRIES = 2000000        # Number of random numbers to generate
gsum = 0.0
ggsum = 0.0
N = 0                   # Keep track of number of accepted values 
TWOPIE = 2.0*math.pi

samples = []            # List of sampled x values

for i in range(NTRIES):

    u = random.uniform(0.0,1.0)  # standard uniform random numbers in range (0,1)

# Use x_3 solution of the cubic, x**3 - 3 x + 2 u = 0 (See NR. 5.6.12).
    x = -2*math.cos( (math.acos(u) - TWOPIE)/3 ) 
    
# Double-check x is in correct range
    if x < 0.0 or x > 1.0:
        print("sampled x value is out of range! ERROR ",x)

    samples.append(x)            # append x to the list of sampled values

    N +=1                        # In this case all candidate (u1, u2) values lead to acceptance
    h = math.cos(0.5*math.pi*x)  # the original integrand
    fp = 1.5*(1.0-x**2)          # the sampling pdf
    g = h/fp                     # the new integrand to be sampled with fp 
    gsum += g                    
    ggsum += g*g

gtrue = (2.0/math.pi)                          # The analytical value of the integral

summary(N, NTRIES, SEED, gsum, ggsum, gtrue)   # Statistical summary

runKSTest(samples)                             # KS test to check that samples is as expected
