from matplotlib import pyplot as plt
import numpy as np
import pylab
import plotfn                    # Various customized plotting functions
from testGaussian import StandardGaussian as model

x = np.linspace(-2.0, 2.0, 10000)

plotfn.PlotCustomize()               # Customize fonts and font sizes etc


ymodel = model(x) 
plotfn.PlotModel5(1, x, ymodel, ' ', r'x', r'Standard Normal pdf', r' pdf')

plt.legend()
plt.grid()

plt.show()
