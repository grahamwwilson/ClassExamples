# pyROOT version of plot.C ROOT macro
#
# Reads histogram from file and does some graphics customizations 
# to make more presentable. Here we use argparse to make the options 
# run time configurable.
#
from ROOT import TCanvas,TFile,gROOT
import argparse

# It is helpful to keep the short and long keywords (y0, ymn) short so as to only occupy one line of the help message
parser = argparse.ArgumentParser(description='Plot histogram from ROOT file and save to graphics file')
parser.add_argument("-hid", "--hid", type=str, default="h1", help="Histogram ID string")
parser.add_argument("-y0", "--ymn", type=float, default=0.0, help="ymin")
parser.add_argument("-y1", "--ymx", type=float, default=600.0, help="ymax")
parser.add_argument("-f", "--file", type=str, default="histos-Pie.root", help="ROOT input file")
parser.add_argument("-t", "--htit", type=str, default="My Histogram Title", help="histogram title")

args=parser.parse_args()
print('Found argument list: ',args)

hist = args.hid
ymin = args.ymn
ymax = args.ymx
rootfile = args.file
htitle = args.htit

# Canvas definition and customization
c = TCanvas("c","multipads",800,600)
c.SetTicks(1,1)
c.SetGrid()

# Define input file and see contents
f = TFile(rootfile)
f.ls()

# Retrieve specified histogram file and customize graphics
h = gROOT.FindObject(hist)
h.GetYaxis().SetTitleOffset(1.4)
h.SetMinimum(ymin)
h.SetMaximum(ymax)
h.SetLineColor(4)    # 4 = blue
h.SetLineWidth(2)
h.SetTitle(htitle)
# If you need these to be set and customized also add as an argument like htitle above.
#h.GetXaxis().SetTitle("Random variate value")
#h.GetYaxis().SetTitle("Random variates per bin")
h.Draw("ehist")

# Save plot as pdf file. One could also customize this using an input argument.
c.Print("PlotPyArg2.pdf")
