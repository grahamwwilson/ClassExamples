# pvalue.py

import myPythonCheck
import pvalueArgs
import numpy as np
from scipy import stats                       

myPythonCheck.Check()                         # Enforce use of python3

chsq, ndof = pvalueArgs.getArguments(None)
pvalueArgs.showArgs(chsq, ndof)

# Calculate upper tail probability assuming the 
# observed chi**2 value, chisq, is a random variate from 
# the Chi-Squared distribution with ndof degrees of freedom

pvaluepercent = 100.0*(1.0 - stats.chi2.cdf(chsq, ndof ))
print(' ')
print('Observed chi-squared p-value of',pvaluepercent,'%')

# Also calculate standardized z-score
# note that this retains the intrinsic asymmetry of the chi-squared distribution
# and is NOT the Gaussian equivalent z-score from the p-value.
z = (chsq - ndof)/np.sqrt(2.0*ndof)
print('Normalized deviation = ',z)

# A p-value exceeding 5% say should happen 95% of the time 
# when the model is correct. One therefore needs to have 
# a low p-value to have significant evidence to reject the  
# null hypothesis.
