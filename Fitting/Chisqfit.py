from matplotlib import pyplot as plt
import numpy as np
from iminuit import Minuit
from scipy.stats import chi2

# line model
def line(x, c, m):
    return m*x + c
    
def custom_chisq(c, m):
    """ Chi-squared function to be minimized """
    ym = line(x_data, c, m)
    z = (y_data - ym)/yerr_data
#    print('ym = ',ym)
#    print('z  = ',z)
    chisq = np.sum(z**2)
    print('Chisq = ',chisq,'for c,m = ',c,m) 
    return chisq

# generate random toy data with random offsets in y 
seed = 26
np.random.seed(seed)
print('seed',seed)
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

m = Minuit(custom_chisq, c = 0.0, m = 0.0)  # starting values for intercept (c) and slope (m) parameters

m.errordef = 1.0 # Corresponds to change in function value associated with +- 1 standard error 
m.migrad()  # finds minimum of least_squares function
m.hesse()   # accurately computes uncertainties

# draw data and fitted line
plt.errorbar(x_data, y_data, yerr_data, fmt="o", label="Data")
plt.plot(x_data, line(x_data, *m.values), label="Line fit")

# display legend with some fit info
fit_info = [
    f"$\\chi^2$ / $n_\\mathrm{{dof}}$ = {m.fval:.2f} / {len(x_data) - m.nfit}",
]
for p, v, e in zip(m.parameters, m.values, m.errors):
    fit_info.append(f"{p} = ${v:.3f} \\pm {e:.3f}$")

plt.legend(title="\n".join(fit_info))

print('Best fit function value (Chi-squared):',m.fval,' for ndof = ',len(x_data)-m.nfit)
ndof = len(x_data)-m.nfit
print('p-value =',1.0-chi2.cdf(m.fval, ndof))
print('Fitted parameter values ',m.values)
print('Fitted parameter errors ',m.errors)
print('Fitted parameter correlation coefficient matrix:')
print(m.covariance.correlation())

plt.show(block=False)
plt.pause(10)   # Keep on-screen for 10s
