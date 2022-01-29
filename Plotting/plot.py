# pyROOT version of plot.C ROOT macro
#
# Reads histogram from file and does some graphics customizations 
# to make more presentable
#
from ROOT import TCanvas,TFile,gROOT

hist = "hgau"
ymin = 0.0
ymax = 1800.0

# Canvas definition and customization
c = TCanvas("c","multipads",800,600)
c.SetTicks(1,1)
c.SetGrid()

# Define input file and see contents
f = TFile("histos-random.root")
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
c.Print("PlotPy.pdf")
