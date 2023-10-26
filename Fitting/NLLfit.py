from matplotlib import pyplot as plt
import numpy as np
from iminuit import Minuit

# line model
def line(x, c, m):
    return m*x + c
    
def custom_nll(c, m):
    """ -2 negative-log-likelihood function to be minimized"""
    ym = line(x_data, c, m)
    z = (y_data - ym)/yerr_data
    p = (1.0/(np.sqrt(2.0*np.pi)*yerr_data))*np.exp(-0.5*z**2)
    nll = -2.0*np.sum(np.log(p))   # Use factor of 2 so that uncertainty intervals are same as for chi-squared
    print('-2lnL = ',nll,'for c,m = ',c,m)
    return nll

# generate random toy data with random offsets in y 
np.random.seed(26)
x_data = np.linspace(-1.0, 1.0, 21)
yerr_data = 0.1 + 0.05*x_data    # Make assumed Gaussian uncertainties increase with increasing x.
c_true = 1.0
m_true = 2.0
y_true = line(x_data, c_true, m_true)
ran = np.random.randn(len(x_data))
y_data = y_true + yerr_data * ran  # Use standard normal random numbers

print('x_data:',x_data)
print('y_true:',y_true)
print('ran:',ran)
print('y_data:',y_data)
print('yerr_data:',yerr_data)

# draw toy data
plt.errorbar(x_data, y_data, yerr_data, fmt="o")

m = Minuit(custom_nll, c=0.0, m=0.0)  # starting values for intercept (c) and slope (m) parameters

m.errordef=1.0
m.migrad()  # finds minimum of least_squares function
m.hesse()   # accurately computes uncertainties

# draw data and fitted line
plt.errorbar(x_data, y_data, yerr_data, fmt="o", label="Data")
plt.plot(x_data, line(x_data, *m.values), label="Line fit")

fit_info = [
    f" -2 lnL = {m.fval:.2f} ",
]
for p, v, e in zip(m.parameters, m.values, m.errors):
    fit_info.append(f"{p} = ${v:.3f} \\pm {e:.3f}$")

plt.legend(title="\n".join(fit_info))

print('Best fit function value (-2lnL):',m.fval)
print('Fitted parameter values ',m.values)
print('Fitted parameter errors ',m.errors)
print('Fitted parameter correlation coefficient matrix:')
print(m.covariance.correlation())

plt.show(block=False)
plt.pause(10)   # Keep on-screen for 10s
