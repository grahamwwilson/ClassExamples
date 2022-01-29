# NewCircle.py
import random
import math
import Pie
import ROOT

# Histogram initialization
f = ROOT.TFile("histos-Pie.root", "recreate")
h0 = ROOT.TH1D("h0","h0; Successes",200,264.25,364.25)
h1 = ROOT.TH1D("h1","h1; Pi Estimate",400,2.6,3.6)
h2 = ROOT.TH1D("h2","h2; Normalized Deviation",200,-5.0,5.0)

for i in range(10000):
    SEED = 200 + i
    mytuple = Pie.PiEstimate(SEED)
    h0.Fill(mytuple[0])
    h1.Fill(mytuple[1])
    error = 0.01*mytuple[2]*math.pi
    ndev = (mytuple[1] - math.pi)/error
    h2.Fill(ndev)

h0.Draw()
h1.Draw()
h2.Draw()
f.Write()
