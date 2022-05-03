import multiprocessing as mp
import math
import random
import os
from timeit import default_timer as timer
# See https://docs.python.org/3/library/multiprocessing.html for more details of multiprocessing

def rndmfunc(iseed):

    print('Initializing random number seed ',iseed,' with pid ',os.getpid())
    random.seed(iseed)
 
# XYVAL is 1/sqrt(2) 
    
# Use importance sampling so that more of the random numbers are useful    
    nhits = 0
    for i in range(N):
        x = random.uniform(XYVAL, 1.0)
        y = random.uniform(0.0 ,XYVAL)
        rsq = x**2 + y**2
        if rsq <=1.0:
            nhits += 1
    return nhits
    
def binomialEfficiency(Ntotal, Nhitsall):
# return probability and binomial uncertainty
    
    p = Nhitsall/Ntotal
    var = Ntotal*p*(1.0-p)
    dp = math.sqrt(var)/Ntotal
    return p,dp

if __name__ == '__main__':   # for safe importing of main module

    start_time = timer()

    Ntotal = 36*10**7
    XYVAL = 1.0/math.sqrt(2.0)
    seed = 1001

    print('Number of cpus : ', mp.cpu_count())
    nprocs = 12
    N = Ntotal//nprocs
    print('Requesting ',N,'trials per process with',nprocs,'processes - total trial count = ',Ntotal)
    pool = mp.Pool(processes=nprocs)
    results = pool.map(rndmfunc, range(seed,seed+nprocs))

    print(results)
    Nhitsall = sum(results)
    print(Nhitsall)
    
    print(' ')
    
    p,dp = binomialEfficiency(Ntotal, Nhitsall)
    print('p = ',p,'dp = ',dp)
    
    fest = XYVAL**2 + 2.0*XYVAL*(1.0-XYVAL)*p
    pie_estimate    = 4.0*fest
    pie_uncertainty = 4.0*(2.0*XYVAL*(1.0-XYVAL)*dp)
    dev = pie_estimate - math.pi
    ndev = dev/pie_uncertainty
    
    print('Estimate of pi            :',pie_estimate,' +- ',pie_uncertainty) 
    print('Fractional uncertainty (%):',100.0*pie_uncertainty/math.pi)
    print(' ')
    print('Deviation from pi         :',dev,' ( ',ndev,' standard deviations )')
    print('Fractional deviation (%)  :',100.0*dev/math.pi)
    
    end_time = timer()
    print(' ')
    print('Execution time ',end_time-start_time)
