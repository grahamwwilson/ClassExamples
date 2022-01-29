import scipy
from scipy.special import comb

#Check scipy version
print('scipy version',scipy.__version__)

#find combinations of 5, 2 values using comb(N, k)
combos = comb(5, 2, exact = False, repetition=True)
print('number of combinations: ',int(combos))
