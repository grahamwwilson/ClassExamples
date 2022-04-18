import numpy as np
from scipy import stats
from scipy.special import comb
from iminuit.util import describe, make_func_code
import math

class LeastSquares:
# Generic least-squares cost function with errors
    def __init__(self, model, x, y, yerr):
        self.model = model  # model predicts y for given x
        self.x    = x
        self.y    = y
        self.yerr = yerr

    def __call__(self, *par):  # we accept a variable number of model parameters in the function call
        ym = self.model(self.x, *par)

        debug = int(0)    # Set to 1 if you want to see what happens here
        if debug==1:      # This printing block will occur on every function call if true)
           print('Number of parameters', len(par) )
           names = describe(self.model)[1:]
           for i in range(0,len(par)):
               print('Parameter',i,': name =',names[i],', value =',par[i])

        chi2 = np.sum( ((self.y - ym)/(self.yerr))**2)
        return chi2

    def runspvalue(self, *par):
#
# Gather information for the "run test". 
# This method needs to be passed the fit parameters, and is expected to be 
# run after a hopefully successful fit.
#
# Note that this statistical test should only be used in principle for 
# simple hypotheses. Example: those with no parameters being fitted to the data.
# In practice it is likely a very useful/pragmatic additional tool even if this 
# theoretical condition is violated.
# 
# The return value is the p-value in per cent.
#
        signs = []  
        residuals = []
        nresiduals = []
        print('Number of parameters', len(par) )
        names = describe(self.model)[1:]
        print(names)
        for i in range(0,len(par)):
            print('Parameter',i,': name =',names[i],', value =',par[i])
        npos = 0
        nrun = 0
        previous = -2
        for i in range(0,self.x.size):
           ymodel = self.model(self.x[i], *par)
           residual = self.y[i] - ymodel
           nresidual = residual/self.yerr[i]
           residuals.append(residual)
           nresiduals.append(nresidual)
           if nresidual > 0.0:
              npos += 1
              value = 1
              signs.append(value)
           else:
              value = 0
              signs.append(value)
           if value != previous:
              nrun +=1
              previous = value

        print(' ')
        nresFormat = len(nresiduals) * '{:>8.2f}'
        nresidualsFormattedList = nresFormat.format(*nresiduals)
        print('Normalized Residuals : ',nresidualsFormattedList)
# For printing clarity, use a binary notation, namely 1 for +ve, 0, for -ve.
        print(' ')
        print('                                   RUN TEST STATISTICS ')
        print(' ')
        signsFormat = len(signs) * '{:1}'
        signsFormattedList = signsFormat.format(*signs)
        print('Residual signs : ',signsFormattedList)
        print('Nbins                     : ',self.x.size)
        print('npos                      : ',npos)
        print('number of runs, r         : ',nrun)
        r = nrun
        N = self.x.size
        NA = npos
        NB = N-NA
        expectedr = 1 + (2*NA*NB/N)
        variancer = 2*NA*NB*(2*NA*NB-N)/(N*N*(N-1))
        print('E(r)                      : ',expectedr)
        print('V(r)                      : ',variancer)
# Estimate the critical value using 5% one-sided confidence level
        zvalue = -999.0
        if variancer > 0.0:        #Protect against zero variance ..
           zvalue = (r-expectedr)/np.sqrt(variancer)
           print('z (sigma)                 : ',zvalue)
           pvaluepercent = 100.0*stats.norm.cdf(zvalue)
           print('p-value (%) normal approx : ',pvaluepercent)
        else: 
           print('Variance is zero ... ')
#
# Do more exact confidence levels 
# using Wald-Wolfowitz run-test expressions using binomial coefficients.
#
# There are dangers here that these expressions end up exceeding the range that 
# is correctly represented using eg. float64 numbers when N is large (eg. N=300).
# With scipy.special.comb and exact=True one gets arbitrary precision integers
# which should avoid this potential pitfall.
#
#        print('nCr (300,150) = ',comb(300,150,exact=True))
#        print('nCr (N,NA) = ',comb(N,NA,exact=True))

        psum = 0.0
        denom = comb(N,NA,exact=True)

# Evaluate run test p-value. See Eadie, p263.
# comb(n,k) = Binomial(n,k) is the binomial coefficient, n!/(k! (n-k)!)
# Calculations were verified with Mathematica for test case of (N,NA,robs) = (100,49,56)
        debug = int(0)    # set to 1 if you want more details
        for i in range(0,r+1):
            if i%2 == 0:          #even
               s = int(i/2)
               p = float(2*comb(NA-1,s-1,True)*comb(NB-1,s-1,True)/denom)
               if debug==1:
                  print('Even: i,s,p = ',i,s,p)
               psum += p
            else:                 #odd
               s = int((i+1)/2)
               p = float((comb(NA-1,s-2,True)*comb(NB-1,s-1,True) + comb(NA-1,s-1,True)*comb(NB-1,s-2,True))/denom)
               if debug==1:
                  print('Odd : i,s,p = ',i,s,p)
               psum += p
        print('Run test p-value for robs <= ',r,' is ',100.0*psum,'(%)')
        print(' ')

        return 100.0*psum

class LsqDriver(LeastSquares):
# LsqDriver class inheriting from LeastSquares
    def __init__(self, model, x, y, yerr):
        super().__init__(model, x, y, yerr)
# Find the model parameters (eg. ['slope', 'intercept'], ['a', 'b', 'c'] etc)
        self.func_code = make_func_code(describe(model)[1:])
        print('This shows partly how the func_code thing works:')
        print(self.func_code) 
