import multiprocessing as mp
import random
import os
from timeit import default_timer as timer

def rndmfunc(iseed):
    print('Initializing random number seed ',iseed,' with pid ',os.getpid())
    random.seed(iseed)
    
    N = 40000000
    x = 0.0
    for i in range(N):
        x = x + random.uniform(-0.5,0.5)
    return x

start_time = timer()
pool = mp.Pool(processes=8)
results = pool.map(rndmfunc, range(1,9))
print(type(results))
print(results)
end_time = timer()
print('Execution time ',end_time-start_time)
