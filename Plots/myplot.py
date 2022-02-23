from matplotlib import pyplot as plt
import numpy as np
import mymodels
import pylab
import plotfn                    # Various customized plotting functions

x, y, dy = pylab.genfromtxt('measurements.dat',usecols=(0,1,2),unpack=True)

print(x)
print(y)
print(dy)

plotfn.PlotCustomize()           # Customize fonts and font sizes etc
plotfn.PlotData(0, x, y, dy, 'Measurements.dat', 'x', 'y')

ymodel1 = mymodels.linemodel(x, 0.95, 0.0)         # constant
ymodel2 = mymodels.linemodel(x, 0.95, 0.05)        # line with a non-zero slope
ymodel3 = mymodels.quadmodel(x, 0.95, 0.0, 0.12)   # parabola

plotfn.PlotDataModel(1, x, y, dy, ymodel1, 'Measurements.dat with model 1', 'x', 'y')
plotfn.PlotDataModel(2, x, y, dy, ymodel2, 'Measurements.dat with model 2', 'x', 'y')
plotfn.PlotDataModel(3, x, y, dy, ymodel3, 'Measurements.dat with model 3', 'x', 'y')

chi = (y - ymodel2)/dy
chisq = chi**2
print('chi',chi)
print('chisq',chisq)
print('Chi-squared sum ',np.sum(chisq))

plt.show()
