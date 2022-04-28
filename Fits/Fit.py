#
# HW3 fits using iminuit for fitting
# Models 1,2,3 as specified in HW3
# Model 4 is a straight line model
# Model 5 is a quadratic model
# Model 6 is the quadratic model with a1=0. (parabola centered on x=0)
#
from matplotlib import pyplot as plt
import numpy as np
import pylab
import plotfn                    # Various customized plotting functions
import fitconfig                 # Put the fit configurations here

x, y, dy = pylab.genfromtxt('measurements.dat',usecols=(0,1,2),unpack=True)
print(x)
print(y)
print(dy)

plotfn.PlotCustomize()                # Customize fonts and font sizes etc

plotfn.PlotDataWithGrid(1, x, y, dy, 'Measurements.dat', 'x', 'y')
   
# Fit model 6
model   = fitconfig.FitModel6(x, y, dy)

# Show the fitted model superimposed on the plot
plotfn.PlotModel3(1, x, model, 'Measurements.dat', 'x', 'y', 'Model 6', 'lime')
plt.legend(loc='upper left')

plt.show()
