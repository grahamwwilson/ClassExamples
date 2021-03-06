# Circle.py
import random
import math

# Illustrate use of random numbers for integration using 
# introductory dart-board example

# Initialize the random number generator using specified seed
SEED = 203
random.seed(SEED)

NINSTANCES = 4000000    # Number of experiments to run
NTOPRINT = 10           # Number of experiments to print

# Keep track of number within unit circle of radius, 1.0
ncircle = 0

# Generate multiple sets of two uniform random numbers each 
# in the range (-1.0,1.0). So random points inside a square with 
# sides of length 2 centered on (0,0)
# The square has an area of 2*2 = 4 units. 
# What is the area of the circle with radius 1?

for i in range(NINSTANCES):
    x = random.uniform(-1.0,1.0)
    y = random.uniform(-1.0,1.0)
# calculate the distance from the origin
    r = math.sqrt(x*x + y*y)
    if r < 1.0:
       ncircle += 1   # point is inside the circle, so count it
    if i < NTOPRINT:
        print('Trial ',i,' x = ',x,' y = ',y,' r = ',r)

print('Number of trial (x,y) values that are inside the circle of radius 1.0 = ',ncircle)

#Add extra code here from circle.txt
fraction = float(ncircle)/float(NINSTANCES)
print('fraction ',fraction)
print('4*fraction ',4.0*fraction)

p = fraction
dNobs = math.sqrt(float(NINSTANCES)*p*(1.0-p))   # Binomial error on success number (ncircle)
dp = dNobs/float(NINSTANCES)

mypi = 4.0*p
dmypi = 4.0*dp
print('Estimate of pi = ',mypi,' +- ',dmypi)
pcdeviation = 100.0*(mypi - math.pi)/math.pi
print('This deviates from ',math.pi,' by ',pcdeviation,'%')
print('The rel. statistical uncertainty is ',100.0*dmypi/mypi,'%')

