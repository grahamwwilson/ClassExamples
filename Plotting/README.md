# ClassExamples/Plotting
These examples use ROOT, mostly the python version, usually called pyROOT

## testrandom.py
Demo example using ROOT to create plots and histograms related to random numbers 
that are saved to an output ROOT file called histos-random.root

## plot.C
Traditional C/C++ macro used to customize the graphics presentation of 
a particular histogram from inside the ROOT interpreter. 
It assumes the histograms are in the file named histos-random.root in the 
local direcotry.
Need to do ($ root -l) followed by (root> .x plot.C ) and (root> .q ) to run it 
and exit from ROOT. Result is a graphics file Plot.pdf.

## MakePlots.sh
Command line example of running plot.C three different times 
with customized options with renaming the output file 
appropriately. See Plot-Gaussian.pdf, Plot-Uniform.pdf, Plot-Exponential.pdf files.
Need to do ($ ./MakePlots.sh )

## plot.py
Example similar to plot.C but in python.
Result is a graphics file PlotPy.pdf.

## plotarg.py
Example similar to plot.py but using argparse for execution time customization.
Do ($ python3 plotarg.py --help ) to see the argument options.
Do ($ python3 plotarg.py -hid "hexp" -y1 1000.0) for example.
Result is a graphics file PlotPyArg.pdf.

## plotarg2.py
Example similar to plotarg.py but defaults to histos-Pie.root 
(which can be produced by running ../MC-Pi/dcCircle.py 
or ../MC-Pi/ntCircle.py or ../MC-Pi/NewCircle.py.
Result is a graphics file PlotPyArg2.pdf.

## clean.sh
Remove root, pdf and png files in local directory. ($ ./clean.sh )
