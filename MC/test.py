import random
import math
import argparse
from scipy import stats

def Gaussian(x):
    """ Standard normal distribution probability density function """
    value = (1.0/math.sqrt(2.0*math.pi))*math.exp(-0.5*x**2)
    return value
    
def main(ngen, seed, which):
    """ Evaluate integral of standard normal distribution from (-2, 2) using Monte Carlo based methods """
 
    Itrue = stats.chi2.cdf(4.0,1)
    
    print('Correct answer',Itrue)

    random.seed(seed)
 
    C = (1.0/math.sqrt(2.0*math.pi))
    print('C = ',C)

    nhits = 0
    fsum = 0.0
    ffsum = 0.0
    area = C*4.0

    integrationVolume = 4.0

    for i in range(ngen):
        x = random.uniform(-2.0,2.0)
        u = random.uniform(0.0,1.0)
        ytest = C*u
        func = Gaussian(x)
        fsum += func
        ffsum += func*func
        if ytest <= func:
            nhits +=1   # accept
            
    print('nhits = ',nhits)
    fmean = fsum/float(ngen)
    ffmean = ffsum/float(ngen) 
    print('<f> = ',fmean)
    varf = ffmean - fmean**2
    error = math.sqrt(varf/float(ngen))
    
    phit = float(nhits)/float(ngen)
    perr  = math.sqrt(phit*(1.0-phit)/float(ngen))
    
    print('Integral Method 1 ',area*phit,' +- ',area*perr)
    print('Integral Method 2 ',integrationVolume*fmean,' +- ',integrationVolume*error)
    
    I1 = area*phit
    dI1 = area*perr
    I2 = integrationVolume*fmean
    dI2 = integrationVolume*error
    
    print('Integral Method 1 error',(I1 - Itrue),' ',(I1-Itrue)/dI1)
    print('Integral Method 2 error',(I2 - Itrue),' ',(I2-Itrue)/dI2)    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Random number generation')
    parser.add_argument("-n", "--ngen", type=int, default=1000000, help="Number of random numbers to generate")
    parser.add_argument("-s", "--seed", type=int, default=208,   help="Random number seed")
    parser.add_argument("-w", "--which", type=int, default=1,   help="Method")    
    
    args=parser.parse_args()
    print('Found argument list: ',args)
    
    main(args.ngen, args.seed, args.which)
