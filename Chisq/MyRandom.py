# MyRandom.py
# 
# Use main based organization with the main conditional handling argument parsing
#
import random
import math
import numpy as np
import matplotlib.pyplot as plot
import argparse

# Global variables
ndof = 1            # number of degrees of freedom for chi-squared distributions
meanPoisson = 2.5   # mean of the Poisson distribution
    
def generateRandomNumbers(N, which):
    """ generate one experiment with N random numbers and return a list with the random numbers 
        which chooses from the following probability distributions
        
        uniform: standard uniform.  r ~ Un (0, 1)
        
        gauss:   standard normal (aka gaussian)   r ~ N (0, 1)
        
        pie2: Bernouilli distribution with success probability, p = pi/4
              random number is r = 1 with probability p, and r = 0, with probability 1-p.
        
        pie3: Bernouilli distribution with success probability, p = pi/6
              random number is r = 1 with probability p, and r = 0, with probability 1-p.
              
        chisq: Chi-squared distribution with ndof degrees of freedom      
              
        expo: Exponential distribution with rate parameter, lambda=1.0 
        
        poisson: Poisson distribution with mean, meanPoisson

    """
    rlist=[]
    for i in range(N):
        if which == 'uniform':
            r = random.uniform(0.0,1.0) # standard uniform random numbers in range [0.0,1.0)
        elif which == 'gauss':
            r = random.gauss(0.0,1.0)   # standard normal distribution (mean = 0.0, rms = 1.0)
        elif which == 'pie2':
    # Do pi calculation    
            x = random.uniform(-1.0, 1.0)
            y = random.uniform(-1.0, 1.0)
            rsq = x**2 + y**2
            r = 0
            if rsq <= 1.0:
                r = 1
        elif which == 'pie3':
    # Do pi calculation    
            x = random.uniform(-1.0, 1.0)
            y = random.uniform(-1.0, 1.0)
            z = random.uniform(-1.0, 1.0)            
            rsq = x**2 + y**2 + z**2
            r = 0
            if rsq<= 1.0:
                r = 1
        elif which == 'chisq':
            r = 0.0
            for j in range(ndof):
                z = random.gauss(0.0, 1.0)
                r = r + z**2
        elif which == 'poisson':
             r = np.random.poisson(meanPoisson)                              
        else:
            r = random.expovariate(1.0) # exponential distribution with rate parameter, lambda=1.0, p(x) = exp(-x).
        rlist.append(r)
    return rlist
    
def calculateStatistics(xlist, verbose=False):
    " calculate sample statistics from input list returning the mean, standard deviation, and uncertainty on the mean "
    xsum = 0.0
    xxsum = 0.0
    N = float(len(xlist))
    for x in xlist:
        xsum  += x
        xxsum += x*x
    xbar  = xsum/N
    xxbar = xxsum/N
# calculate Bessel's correction so that variance estimate from the sample is unbiased.
# variance is nonsense for N=1. Note that the correction is only really of much relevance for small N.    
    besselCorrection = 1.0       
    if int(N)>1:                      # avoid divide by zero errors if N=1.
       besselCorrection= N/(N-1.0)
    sampleVariance = besselCorrection*(xxbar - xbar**2)
    sampleStandardDeviation = math.sqrt(sampleVariance)
    sampleMean = xbar
    sampleUncertaintyOnMean = sampleStandardDeviation/math.sqrt(N)     # NB the 1/sqrt(N) !
    sampleUncertaintySD = sampleStandardDeviation/math.sqrt(N-1.0)     # Barlow 5.24    
    sampleUncertaintyVariance = sampleVariance*math.sqrt(2.0/(N-1.0))  # Barlow 5.18    
      
    if verbose:
        print(' ')
        print('Summary based on',int(N),'instances')
        print('Observed mean ',sampleMean)
        print('Observed s.d. ',sampleStandardDeviation,' +- ',sampleUncertaintySD)
        print('Observed variance ',sampleVariance,' +- ',sampleUncertaintyVariance)
        print('RESULT <x> = ',sampleMean,' +- ',sampleUncertaintyOnMean)
    
    return sampleMean, sampleStandardDeviation, sampleUncertaintyOnMean
    
def tailProbability(xlist, criticalValue):
    """ Measure the probability of randomly sampled events that would have a value greater than or equal to the 
        critical value strictly by chance. Related closely to the p-value, based on the observed value of the statistic """
        
    N = len(xlist)
    tailNumber = 0
    for x in xlist:
        if x >= criticalValue:
            tailNumber += 1
    
    tailProbability = float(tailNumber)/float(N)
    dp = math.sqrt(tailProbability*(1.0-tailProbability)/float(N))
    print('Measured tail probability of ',tailProbability,' +- ',dp,' for critical value = ',criticalValue)
    print('Corresponding 1-p is ',1.0 - tailProbability,' +- ',dp)
      
def makePlot(mylist, plotfile, bins=[-0.25, 0.25, 0.75, 1.25]):
    " make plot with histogram using discrete bins that emphasize the 0 (failure) or 1 (success) nature of Bernouilli trials"
    plot.hist(mylist, bins) 
    plot.title('1 million Bernouilli trials')
    plot.xlabel('r')
    plot.ylabel('Instances per bin')
    
    plot.show(block=False)
    plot.pause(10)
    plot.savefig(plotfile)              # Save plot to file
    plot.close()
    
def makePlot2(mylist, plotfile, title):
    " make plot with histogram"
    plot.hist(mylist, 50) 
    plot.title(title)
    plot.xlabel('r')
    plot.ylabel('Instances per bin')
    
    plot.show(block=False)
    plot.pause(10)
    plot.savefig(plotfile)              # Save plot to file
    plot.close()    

def piEstimates(which, mean, meanUncertainty):
    " make pi estimate calculations "
    
    alpha = 6.0                # p = pi/6   => pi = 6*p
    if which == "pie2":
        alpha = 4.0            # p = pi/4   => pi = 4*p
        
    piEstimate = alpha*mean
    piEstimateUncertainty = alpha*meanUncertainty
    fractionalUncertainty = piEstimateUncertainty/piEstimate

    piTrue = math.pi
    deviation = piEstimate - piTrue
    fractionalDeviation = deviation/piTrue
    percentDeviation = 100.0*fractionalDeviation
    standardizedDeviation = deviation/piEstimateUncertainty
    
    print("    ")
    print("Measured value of pi = ",piEstimate,"+-",piEstimateUncertainty)
    print("    ")
    print("Fractional Uncertainty ",fractionalUncertainty)
    print("Deviation              ",deviation)
    print("Fractional Deviation   ",fractionalDeviation)
    print("% deviation            ",percentDeviation)
    print("Standardized Deviation ",standardizedDeviation)

def main(ngen, seed, which, plotfile, criticalValue, title):
    " python main function to generate random numbers, make statistics, and make plot "
# Initialize the random number generator using specified seed
    random.seed(seed)
    np.random.seed(seed)   # Also reset the numpy based random numbers 

# Generate random numbers returning the list of observed random variates
    rList = generateRandomNumbers(ngen, which)
    
# Calculate statistics associated with the list.
    mean, sd, meanUncertainty = calculateStatistics(rList, True) 
    
# Calculate pi from the Bernouilli probability estimates if requested
    if which=='pie2' or which=='pie3':
        piEstimates(which, mean, meanUncertainty)

    tailProbability(rList, criticalValue)
        
# Plot the distribution of the random variates saving the plot to a file
    makePlot2(rList,plotfile,title)

if __name__ == '__main__':
    # execute only if run as a script / from the command line
    print('Executing the MyRandom.py main conditional statements')  # Add print for clarity on execution mode
        
    parser = argparse.ArgumentParser(description='Random number generation')
    parser.add_argument("-n", "--ngen", type=int, default=100000, help="Number of random numbers to generate")
    parser.add_argument("-d", "--ndof", type=int, default=5, help="Number of degrees of freedom for chi-squared distribution") 
    parser.add_argument("-c", "--crit", type=float, default=1.0, help="Critical value") 
    parser.add_argument("-m", "--pmu", type=float, default=2.5, help="Poisson mean")
    parser.add_argument("-t", "--tit", type=str, default="Chi-squared distributions", help="Plot title string")                
    parser.add_argument("-s", "--seed", type=int, default=208,   help="Random number seed")
    parser.add_argument("-w", "--which", type=str, default="chisq", help="Random number distribution (uniform/gauss/expo/pie2/pie3/chisq/poisson)")
    parser.add_argument("-p", "--plotfile", type=str, default="chisq.png", help="Graphics file")    

    args=parser.parse_args()
    print('Found argument list: ',args)
    
# Set global variable
    ndof = args.ndof
    meanPoisson = args.pmu
    
    main(args.ngen, args.seed, args.which, args.plotfile, args.crit, args.tit)
