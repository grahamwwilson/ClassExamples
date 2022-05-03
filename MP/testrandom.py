import multiprocessing as mp
import random
import os
from timeit import default_timer as timer
# See https://docs.python.org/3/library/multiprocessing.html for more details of multiprocessing

def rndmfunc(iseed):
    print('Initializing random number seed ',iseed,' with pid ',os.getpid())
    random.seed(iseed)
    
    N = 40000000
    x = 0.0
    for i in range(N):
        x = x + random.uniform(-0.5,0.5)
    return x

if __name__ == '__main__':   # for safe importing of main module

    start_time = timer()

    print("Number of cpus : ", mp.cpu_count())
    pool = mp.Pool(processes=12)
    results = pool.map(rndmfunc, range(1,13))

    print(results)
    
    end_time = timer()
    print('Execution time ',end_time-start_time)
