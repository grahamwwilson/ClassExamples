# Uniformed.py
# 
# Restructure to use main organization
#
import random
import math
import matplotlib.pyplot as plot
import argparse

def generateRandomNumbers(N):
    " generate N random numbers from Uniform distribution on [0.0, 1.0) "
    ulist=[]
    for i in range(N):
        u = random.uniform(0.0,1.0) # standard uniform random numbers 
                            # in range [0.0,1.0)
        ulist.append(u)
    return ulist
    
def calculateStatistics(xlist):
    " calculate sample statistics from input list "
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
    print('Summary based on',int(N),'instances')
    print('Observed mean ',xbar)
    print('Observed rms ',sampleStandardDeviation)
    print('RESULT <u> = ',xbar,' +- ',sampleStandardDeviation/math.sqrt(N))
     
def makePlot(mylist, nbins):
    " make plot with uniform distribution histogram with specified number of bins, nbins "
    plot.hist(mylist, bins=nbins)
    plot.title('Uniform Distribution Histogram')
    plot.xlabel('u')
    plot.ylabel('Instances per bin')
    
    plot.show(block=False)
    plot.pause(3)
    plot.close()

def main(ngen, seed, nbins):
    " python main function to generate random numbers, make statistics, and make plot "
# Initialize the random number generator using specified seed
    random.seed(seed)

# Generate random numbers returning list
    ulist = generateRandomNumbers(ngen)

# Calculate statistics using the list
    calculateStatistics(ulist)

# Plot the generated data from the list
    makePlot(ulist,nbins)

if __name__ == '__main__':
    # This executes only if run as a script / from the command line
    print('Executing the Uniformed.py main conditional statements')  # Add print for clarity on execution mode
    
    parser = argparse.ArgumentParser(description='Uniform random number generation')
    parser.add_argument("-n", "--ngen", type=int, default=10000, help="Number of random numbers to generate")
    parser.add_argument("-s", "--seed", type=int, default=203,   help="Random number seed")
    parser.add_argument("--nbins", type=int, default=100, help="Number of histogram bins")

    args=parser.parse_args()
    print('Found argument list: ',args)
    
    main(args.ngen, args.seed, args.nbins)
