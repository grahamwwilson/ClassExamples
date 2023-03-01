from matplotlib import pyplot as plt
import numpy as np
from iminuit import Minuit

# parabola model
def parabola(x, c, m):
    return m*x**2 + c

# line model
def line(x, c, m):
    return m*x + c
    
def custom_least_squares(c, m):
    ym = line(x_data, c, m)
    z = (y_data - ym)/yerr_data
    return np.sum(z**2)

# generate random toy data with random offsets in y 
np.random.seed(23)
x_data = np.linspace(0, 1, 11)
yerr_data = 0.1 + 0.1*x_data    # Make assumed Gaussian uncertainties increase with increasing x.
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

m = Minuit(custom_least_squares, c=0.0, m=0.0)  # starting values for intercept (c) and slope (m) parameters

m.errordef=1.0
m.migrad()  # finds minimum of least_squares function
m.hesse()   # accurately computes uncertainties

# draw data and fitted line
plt.errorbar(x_data, y_data, yerr_data, fmt="o", label="Data")
plt.plot(x_data, line(x_data, *m.values), label="Line fit")

# display legend with some fit info
fit_info = [
    f"$\\chi^2$ / $n_\\mathrm{{dof}}$ = {m.fval:.1f} / {len(x_data) - m.nfit}",
]
for p, v, e in zip(m.parameters, m.values, m.errors):
    fit_info.append(f"{p} = ${v:.3f} \\pm {e:.3f}$")

plt.legend(title="\n".join(fit_info))

plt.show()
