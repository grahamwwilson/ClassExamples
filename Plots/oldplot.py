from matplotlib import pyplot as plt
import numpy as np
import mymodels
import pylab

x, y, dy = pylab.genfromtxt('measurements.dat',usecols=(0,1,2),unpack=True)

print(x)
print(y)
print(dy)

# 3. Add some plotting customization
SMALL_SIZE = 20
MEDIUM_SIZE = 26
BIGGER_SIZE = 32
plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)     # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)     # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)     # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)     # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)   # fontsize of the figure title

plt.figure(0)
plt.errorbar(x, y, dy, fmt="o",color='blue',solid_capstyle='projecting',capsize=0,markersize=4)
plt.title('Measurements.dat')
plt.xlabel('x')
plt.ylabel('y')

ymodel1 = mymodels.linemodel(x,0.95,0.0)           # constant
ymodel2 = mymodels.linemodel(x,0.95,0.05)         # line with a non-zero slope
print('ymodel2:',ymodel2)
ymodel3 = mymodels.quadmodel(x,0.95,0.0,0.12)     # parabola

plt.figure(1)
plt.errorbar(x, y, dy, fmt="o",color='blue',solid_capstyle='projecting',capsize=0,markersize=4)
plt.plot(x, ymodel1, color='red')
plt.title('Measurements.dat with model 1')
plt.xlabel('x')
plt.ylabel('y')

plt.figure(2)
plt.errorbar(x, y, dy, fmt="o",color='blue',solid_capstyle='projecting',capsize=0,markersize=4)
plt.plot(x, ymodel2, color='red')
plt.title('Measurements.dat with model 2')
plt.xlabel('x')
plt.ylabel('y')

plt.figure(3)
plt.errorbar(x, y, dy, fmt="o",color='blue',solid_capstyle='projecting',capsize=0,markersize=4)
plt.plot(x, ymodel3, color='red')
plt.title('Measurements.dat with model 3')
plt.xlabel('x')
plt.ylabel('y')

chi = (y - ymodel2)/dy
chisq = chi**2
print('chi',chi)
print('chisq',chisq)
print('Chi-squared sum ',np.sum(chisq))

plt.show()
