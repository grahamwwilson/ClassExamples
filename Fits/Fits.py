#
# HW3 fits using iminuit for fitting
# Models 1,2,3 as specified in HW3   (1-parameter)
# Model 4 is a straight line model   (2-parameter)
# Model 5 is a quadratic model       (3-parameter)
# Model 6 is a parabolic model       (2-parameter)
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

plotfn.PlotDataWithGrid(1, x, y, dy, 'Measurements.dat with model 1', 'x', 'y')
plotfn.PlotDataWithGrid(2, x, y, dy, 'Measurements.dat with model 2', 'x', 'y')
plotfn.PlotDataWithGrid(3, x, y, dy, 'Measurements.dat with model 3', 'x', 'y')
plotfn.PlotDataWithGrid(4, x, y, dy, 'Measurements.dat with model 4', 'x', 'y')
plotfn.PlotDataWithGrid(5, x, y, dy, 'Measurements.dat with model 5', 'x', 'y')
plotfn.PlotDataWithGrid(6, x, y, dy, 'Measurements.dat with model 6', 'x', 'y')
   
# Fit models 1,2,3,4,5,6
model1   = fitconfig.FitModel1(x, y, dy)
model2   = fitconfig.FitModel2(x, y, dy)
model3   = fitconfig.FitModel3(x, y, dy)
model4   = fitconfig.FitModel4(x, y, dy)
model5   = fitconfig.FitModel5(x, y, dy)
model6   = fitconfig.FitModel6(x, y, dy)

# We can also now show the fitted models superimposed on the respective plots
plotfn.PlotModel2(1, x, model1, 'Measurements.dat with model 1', 'x', 'y', 'magenta')
plotfn.PlotModel2(2, x, model2, 'Measurements.dat with model 2', 'x', 'y', 'red')
plotfn.PlotModel2(3, x, model3, 'Measurements.dat with model 3', 'x', 'y', 'black')
plotfn.PlotModel2(4, x, model4, 'Measurements.dat with model 4', 'x', 'y', 'cyan')
plotfn.PlotModel2(5, x, model5, 'Measurements.dat with model 5', 'x', 'y', 'lime')
plotfn.PlotModel2(6, x, model6, 'Measurements.dat with model 6', 'x', 'y', 'orange')

# Show all HW3 fits together
plotfn.PlotDataWithGrid(7, x, y, dy, 'Measurements.dat', 'x', 'y')
plotfn.PlotModel3(7, x, model1, 'Measurements.dat', 'x', 'y', 'Model 1', 'magenta')
plotfn.PlotModel3(7, x, model2, 'Measurements.dat', 'x', 'y', 'Model 2', 'red')
plotfn.PlotModel3(7, x, model3, 'Measurements.dat', 'x', 'y', 'Model 3', 'black')
plt.legend(loc='upper left')

# Show the multiparameter fits together
plotfn.PlotDataWithGrid(8, x, y, dy, 'Measurements.dat', 'x', 'y')
plotfn.PlotModel3(8, x, model4, 'Measurements.dat', 'x', 'y', 'Model 4', 'cyan')
plotfn.PlotModel3(8, x, model5, 'Measurements.dat', 'x', 'y', 'Model 5', 'lime')
plotfn.PlotModel3(8, x, model6, 'Measurements.dat', 'x', 'y', 'Model 6', 'orange')
plt.legend(loc='upper left')

# And now for total confusion
plotfn.PlotDataWithGrid(9, x, y, dy, 'Measurements.dat', 'x', 'y')
plotfn.PlotModel3(9, x, model1, 'Measurements.dat', 'x', 'y', 'Model 1', 'magenta')
plotfn.PlotModel3(9, x, model2, 'Measurements.dat', 'x', 'y', 'Model 2', 'red')
plotfn.PlotModel3(9, x, model3, 'Measurements.dat', 'x', 'y', 'Model 3', 'black')
plotfn.PlotModel3(9, x, model4, 'Measurements.dat', 'x', 'y', 'Model 4', 'cyan')
plotfn.PlotModel3(9, x, model5, 'Measurements.dat', 'x', 'y', 'Model 5', 'lime')
plotfn.PlotModel3(9, x, model6, 'Measurements.dat', 'x', 'y', 'Model 6', 'orange')
plt.legend(loc='upper left')

plt.show()
