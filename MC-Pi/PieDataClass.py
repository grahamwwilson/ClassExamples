# PieDataClass.py
import random
import math
from dataclasses import dataclass     #only available in Python 3.7+

@dataclass
class Estimator:
    " Estimator class "
    nsuccesses: int
    estimate: float
    error: float

# Refactor as a function
# Illustrate use of random numbers for integration

def PiEstimate(SEED, N):
    " Estimate pi using N trials with random number, SEED "
# SEED = random number seed
# N    = number of trials 

# Initialize the random number generator using specified seed
    random.seed(SEED)

# Keep track of number within unit circle of radius, 1.0
    ncircle = 0

# Generate multiple sets of two uniform random numbers each 
# in the range (-1.0,1.0). So random points inside a square with 
# sides of length 2 centered on (0,0)
# The square has an area of 2*2 = 4 units. 
# What is the area of the circle with radius 1?

    for i in range(N):
        x = random.uniform(-1.0,1.0)
        y = random.uniform(-1.0,1.0)
# calculate the distance from the origin
        r = math.sqrt(x*x + y*y)
        if r < 1.0:
            ncircle += 1   # point is inside the circle, so count it

    print('Number of trial (x,y) values that are inside the circle of radius 1.0 = ',ncircle)

#Add extra code here from circle.txt
    fraction = float(ncircle)/float(N)
    print('fraction ',fraction)
    print('4*fraction ',4.0*fraction)

    p = fraction
    dNobs = math.sqrt(float(N)*p*(1.0-p))   # Binomial error on success number (ncircle)
    print('Binomial uncertainty on nsuccesses: ',dNobs)
    dp = dNobs/float(N)

    mypi = 4.0*p
    dmypi = 4.0*dp
    print('Estimate of pi = ',mypi,' +- ',dmypi)
    pcdeviation = 100.0*(mypi - math.pi)/math.pi
    print('This deviates from ',math.pi,' by ',pcdeviation,'%')
    print('The rel. statistical uncertainty is ',100.0*dmypi/mypi,'%')
    ptrue = math.pi/4.0
    dNtrue = math.sqrt(float(N)*ptrue*(1.0-ptrue))
    dptrue = dNtrue/float(N)
    dpitrue = 4.0*dptrue
    dstat = 100.0*dpitrue/math.pi
    print('Using correct p, stat. uncertainty on N',dNtrue,' rel. uncertainty ',dstat,'%')
   
    error = dpitrue

# Here we use a dataclass to return the information
    e = Estimator(ncircle,mypi,error)

    return e
