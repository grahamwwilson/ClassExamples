import multiprocessing as mp
def cube(x):
    return x**3

pool = mp.Pool(processes=4)
results = pool.map(cube, range(1,7))
print(results)
