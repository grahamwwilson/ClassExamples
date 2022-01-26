# pyROOT version of plot.C ROOT macro
#
# Reads histogram from file and does some graphics customizations 
# to make more presentable
#
from ROOT import TCanvas,TFile,gROOT
import argparse

parser = argparse.ArgumentParser(description='Plot histogram from file')
parser.add_argument("-hid", "--histid", type=str, default="h1", help="Histogram ID string")
parser.add_argument("-y0", "--ymin", type=float, default=0.0, help="ymin")
parser.add_argument("-y1", "--ymax", type=float, default=1800.0, help="ymax")
parser.add_argument("-f", "--file", type=str, default="histos_Pie.root", help="ROOT input file")

args=parser.parse_args()
print('Found argument list: ',args)

hist = args.histid
ymin = args.ymin
ymax = args.ymax
rootfile = args.file

#hist = "hgau"
#ymin = 0.0
#ymax = 1800.0

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
h.SetLineColor(4)
h.SetLineWidth(2)
h.SetTitle("Probability distributions using random numbers")
h.GetXaxis().SetTitle("Random variate value")
h.GetYaxis().SetTitle("Random variates per bin")
h.Draw("ehist")

# Save plot as pdf file
c.Print("PlotPyArg.pdf")
