# UniformPlotter.py
import random
import math
import matplotlib.pyplot as plot
import argparse

def generateRandomNumbers(N):
    """ generate N random numbers from Uniform distribution on [0.0, 1.0) """
    ulist=[]
    for i in range(N):
        u = random.random() # standard uniform random numbers 
                            # in range [0.0,1.0)
        ulist.append(u)
    return ulist
    
def calculateStatistics(xlist):
    """ calculate sample statistics """
    xsum = 0.0
    xxsum = 0.0
    N = float(len(xlist))
    for x in xlist:
        xsum  += x
        xxsum += x*x
    xbar  = xsum/N
    xxbar = xxsum/N
    besselFactor = N/(N-1.0)
    sampleVariance = besselFactor*(xxbar - xbar**2)
    sampleStandardDeviation = math.sqrt(sampleVariance)
    
    print(' ')
    print('Summary based on',N,'instances')
    print('Observed mean ',xbar)
    print('Observed rms ',sampleStandardDeviation)
    print('RESULT <u> = ',xbar,' +- ',sampleStandardDeviation/math.sqrt(N))
     
def makePlot(mylist, nbins):
    """ Make plot with uniform distribution histogram with specified number of bins, nbins """
    plot.hist(mylist, bins=nbins)
    plot.title('Uniform Distribution Histogram')
    plot.xlabel('u')
    plot.ylabel('Instances per bin')
    plot.show()

parser = argparse.ArgumentParser(description='Uniform random number generation')
parser.add_argument("-n", "--ngen", type=int, default=10000, help="Number of random numbers to generate")
parser.add_argument("-s", "--seed", type=int, default=203,   help="Random number seed")
parser.add_argument("--nbins", type=int, default=100, help="Number of histogram bins")

args=parser.parse_args()
print('Found argument list: ',args)

NGEN  = args.ngen
SEED  = args.seed
NBINS = args.nbins

# Initialize the random number generator using specified seed
random.seed(SEED)

# Generate random numbers returning list
ulist = generateRandomNumbers(NGEN)

# Calculate statistics using the list
calculateStatistics(ulist)

# Plot the generated data
makePlot(ulist,NBINS)
