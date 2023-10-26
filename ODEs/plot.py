from matplotlib import pyplot as plt
import numpy as np
import pylab
import plotfn                    # Various customized plotting functions
import argparse

def main(datfile, title, dt):

    istep, t, theta, omega, Eratio = pylab.genfromtxt(datfile, usecols=(0,1,2,3,4), unpack=True)

    newtitle = title + dt

    plotfn.PlotCustomize()           # Customize fonts and font sizes etc
    plotfn.PlotData(0, t, theta, newtitle, 't (s)', 'Angle (rad)')   
    plotfn.PlotData(1, t, omega, newtitle, 't (s)', 'Angular velocity (rad/s)')
    plotfn.PlotData(2, t, Eratio, newtitle, 't (s)', 'E/E0')

    plt.show()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Plot ODE evolution')
    parser.add_argument("-i", "--infile", type=str, default="pendulum.dat", help="Input file with ODE results")
    parser.add_argument("-t", "--title", type=str, default="Pendulum", help="Plot title")
    parser.add_argument("-d", "--dt", type=str, default=" (RK2: dt = 0.01s)", help="Time step")    
    
    args=parser.parse_args()
    print('Found argument list: ',args)
    
    main(args.infile, args.title, args.dt)
    
