from matplotlib import pyplot as plt
import numpy as np
import pylab
import plotfn                    # Various customized plotting functions
from testIntegral import ExampleIntegrand as model

x = np.linspace(0.0, 2.0*np.pi, 10000)

plotfn.PlotCustomize()               # Customize fonts and font sizes etc


ymodel = model(x) 
plotfn.PlotModel5(1, x, ymodel, ' ', r'x', r'f(x)', r' x^2 cos^4(x)')

plt.legend()
plt.grid()

plt.show()
