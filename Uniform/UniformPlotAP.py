# UniformPlotAP.py
import random
import math
import matplotlib.pyplot as plot
import argparse

# Illustrate standard uniform random number generator

parser = argparse.ArgumentParser(description='Uniform random number demonstration')
parser.add_argument("-n", "--ngen", type=int, default=100, help="Number of random numbers to generate")
parser.add_argument("-s", "--seed", type=int, default=203, help="Random number seed")

args=parser.parse_args()
print('Found argument list: ',args)

NGEN = args.ngen
SEED = args.seed

# Initialize the random number generator using specified seed
random.seed(SEED)

ulist=[]
usum = 0.0
uusum = 0.0

# Generate uniform random numbers
for i in range(NGEN):
    u = random.random() # standard uniform random numbers 
                        # in range [0.0,1.0)
    usum  += u
    uusum += u*u
    ulist.append(u)

# Calculate post-generation statistics
samplemeanu = usum/float(NGEN)
samplemeanuu = uusum/float(NGEN)
besselfactor = float(NGEN)/float(NGEN-1)
samplevariance = besselfactor*(samplemeanuu - samplemeanu*samplemeanu)
samplesd = math.sqrt(samplevariance)

# Summary
print(' ')
print('Summary based on',NGEN,'instances using SEED',SEED)
print('Observed mean ',samplemeanu)
print('Observed rms ',samplesd)
print('RESULT <u> = ',samplemeanu,' +- ',samplesd/math.sqrt(NGEN))

# Plot the generated data
plot.hist(ulist, bins=50)
plot.title('Uniform Distribution Histogram')
plot.xlabel('u')
plot.ylabel('Instances per bin')
plot.show()
