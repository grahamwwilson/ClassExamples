from matplotlib import pyplot as plt
import numpy as np
import pylab
import plotfn                    # Various customized plotting functions

istep, t, theta, omega, Eratio = pylab.genfromtxt('pendulum.dat',usecols=(0,1,2,3,4),unpack=True)

plotfn.PlotCustomize()           # Customize fonts and font sizes etc
plotfn.PlotData(0, t, theta, 'Simple Pendulum', 't (s)', 'theta (rad)')

plt.show()
