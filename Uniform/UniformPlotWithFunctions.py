# UniformPlotWithFunctions.py
import random
import math
import matplotlib.pyplot as plot

def generateRandomNumbers(N):
    """ generate N random numbers from Uniform distribution on [0.0, 1.0) """
    ulist=[]
    for i in range(N):
        u = random.random() # standard uniform random numbers 
                            # in range [0.0,1.0)
        ulist.append(u)
    return ulist
    
def calculateStatistics(mylist):
    """ calculate statistics """
    print("still need to implement calculateStatistics")
     
def makePlot(mylist, nbins):
    plot.hist(mylist, bins=nbins)
    plot.title('Uniform Distribution Histogram')
    plot.xlabel('u')
    plot.ylabel('Instances per bin')
    plot.show()

# Illustrate standard uniform random number generator

SEED  = 203          # random number generator seed
NGEN  = 10000        # number of random numbers to generate
NBINS = 100          # number of bins in the plot

# Initialize the random number generator using specified seed
random.seed(SEED)

# Generate random numbers returning list
ulist = generateRandomNumbers(NGEN)

# Calculate statistics using the list
calculateStatistics(ulist)

# Plot the generated data
makePlot(ulist,NBINS)
