import random
import math
import argparse
import numpy as np
from scipy import stats

def StandardGaussian(x):
    """ Standard normal distribution probability density function """
    f = (1.0/math.sqrt(2.0*math.pi))*np.exp(-0.5*x**2)
    return f
    
def exampleGaussian(ngen, seed):
    """ Evaluate integral of standard normal distribution from (-2, 2) using Monte Carlo based methods """

    Itrue = stats.chi2.cdf(4.0, 1)   
    print('Correct answer',Itrue)

    random.seed(seed)
 
    C = (1.0/math.sqrt(2.0*math.pi)) # max value of function in the [-2.0,2.0] range    
    print('C = ',C)

    nhits = 0

    integrationVolume = 4.0      # Desired integral is 1-d so "integrationVolume" is the length of the x interval
    area = C*integrationVolume   # area tested by hit and miss

# First loop for hit and miss method (Method 1)
    for i in range(ngen):
        x = random.uniform(-2.0,2.0)
        u = random.uniform(0.0,1.0)
        ytest = C*u                   
        func = StandardGaussian(x)
        if ytest <= func:
            nhits +=1   # accept
    print('nhits = ',nhits,' Efficiency = ',100.0*float(nhits)/float(ngen),'%')
    phit = float(nhits)/float(ngen)
    perr  = math.sqrt(phit*(1.0-phit)/float(ngen))
    print('Integral Method 1 (Hit/Miss)',area*phit,' +- ',area*perr)    
                
# Second loop for MC integration by averaging the function (Method 2)
    fsum = 0.0
    ffsum = 0.0
    for j in range(ngen):
        x = random.uniform(-2.0,2.0)       
        func = StandardGaussian(x)
        fsum += func
        ffsum += func*func
         
    fmean = fsum/float(ngen)
    ffmean = ffsum/float(ngen) 
    varf = ffmean - fmean**2    
    print('<f> = ',fmean,'rms = ',math.sqrt(varf))

    error = math.sqrt(varf/float(ngen))
    print('Integral Method 2 (MC      )',integrationVolume*fmean,' +- ',integrationVolume*error)
    
    I1 = area*phit
    dI1 = area*perr
    I2 = integrationVolume*fmean
    dI2 = integrationVolume*error
    
    print('Integral Method 1 deviation, percent uncertainty, significance',(I1 - Itrue),' ',100.0*dI1/Itrue,'% ',(I1-Itrue)/dI1,'sigma')
    print('Integral Method 2 deviation, percent uncertainty, significance',(I2 - Itrue),' ',100.0*dI2/Itrue,'% ',(I2-Itrue)/dI2,'sigma')    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Random number generation')
    parser.add_argument("-n", "--ngen", type=int, default=1000000, help="Number of random numbers to generate")
    parser.add_argument("-s", "--seed", type=int, default=208,     help="Random number seed")
    
    args=parser.parse_args()
    print('Found argument list: ',args)
    
    exampleGaussian(args.ngen, args.seed)
