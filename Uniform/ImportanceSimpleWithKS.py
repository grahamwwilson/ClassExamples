# ImportanceSimpleWithKS.py
import random
import math
from MyKSTest import runKSTest
from Summary import summary

# Illustrate importance sampling for the integral(0,1) of cos(pi x/2). 
# Using fp = 1.5(1 - x^2) for the sampling distribution.
# In this case we apply a recipe for sampling, following the footnote 
# on page 82 of the Kalos and Whitlock book. 
# We also include a KS test to check that the sampled distribution is as expected

SEED = 203
random.seed(SEED)       # Initialize random number generator using specified seed
NTRIES = 1000000        # Number of random numbers to generate
gsum = 0.0
ggsum = 0.0
N = 0                   # Keep track of number of accepted values 

samples = []            # List of sampled x values

for i in range(NTRIES):

    u1 = random.uniform(0.0,1.0) # standard uniform random numbers in range
    u2 = random.uniform(0.0,1.0) # in range (0.0,1.0)

# Use Kalos and Whitlock algorithm
    x = 1.0 - u1
    if u2 > u1*(3.0-u1)/2.0:
        x = 0.5*( math.sqrt(9.0-8.0*u2) - 1.0 )
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
