#!/bin/bash

root -l -b -q 'plot.C()'
mv Plot.pdf Plot_Gaussian.pdf

root -l -b -q 'plot.C("h1","Uniform",0.0,200.0)'
mv Plot.pdf Plot_Uniform.pdf

root -l -b -q 'plot.C("hexp","Exponential",0.0,1000.0)'
mv Plot.pdf Plot_Exponential.pdf

exit
