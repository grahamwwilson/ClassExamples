#
# HW3 fits using iminuit for fitting
# Models 1,2,3 as specified in HW3
# Model 4 is a straight line model
# Model 5 is a quadratic model
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
   
# Fit models 1,2,3,4,5
model1   = fitconfig.FitModel1(x, y, dy)
model2   = fitconfig.FitModel2(x, y, dy)
model3   = fitconfig.FitModel3(x, y, dy)
model4   = fitconfig.FitModel4(x, y, dy)
model5   = fitconfig.FitModel5(x, y, dy)

# We can also now show the fitted models superimposed on the respective plots
plotfn.PlotModel2(1, x, model1, 'Measurements.dat with model 1', 'x', 'y', 'magenta')
plotfn.PlotModel2(2, x, model2, 'Measurements.dat with model 2', 'x', 'y', 'red')
plotfn.PlotModel2(3, x, model3, 'Measurements.dat with model 3', 'x', 'y', 'black')
plotfn.PlotModel2(4, x, model4, 'Measurements.dat with model 4', 'x', 'y', 'cyan')
plotfn.PlotModel2(5, x, model5, 'Measurements.dat with model 5', 'x', 'y', 'lime')

# Show all HW3 fits together
plotfn.PlotDataWithGrid(6, x, y, dy, 'Measurements.dat', 'x', 'y')
plotfn.PlotModel2(6, x, model1, 'Measurements.dat', 'x', 'y', 'magenta')
plotfn.PlotModel2(6, x, model2, 'Measurements.dat', 'x', 'y', 'red')
plotfn.PlotModel2(6, x, model3, 'Measurements.dat', 'x', 'y', 'black')

# Show the reasonable multiparameter fits together
plotfn.PlotDataWithGrid(7, x, y, dy, 'Measurements.dat', 'x', 'y')
plotfn.PlotModel2(7, x, model3, 'Measurements.dat', 'x', 'y', 'black')
plotfn.PlotModel2(7, x, model4, 'Measurements.dat', 'x', 'y', 'cyan')
plotfn.PlotModel2(7, x, model5, 'Measurements.dat', 'x', 'y', 'lime')

# And now for total confusion
plotfn.PlotDataWithGrid(8, x, y, dy, 'Measurements.dat', 'x', 'y')
plotfn.PlotModel2(8, x, model1, 'Measurements.dat', 'x', 'y', 'magenta')
plotfn.PlotModel2(8, x, model2, 'Measurements.dat', 'x', 'y', 'red')
plotfn.PlotModel2(8, x, model3, 'Measurements.dat', 'x', 'y', 'black')
plotfn.PlotModel2(8, x, model4, 'Measurements.dat', 'x', 'y', 'cyan')
plotfn.PlotModel2(8, x, model5, 'Measurements.dat', 'x', 'y', 'lime')

plt.show()
