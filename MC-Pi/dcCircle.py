# dcCircle.py
import random
import math
from PieDataClass import PiEstimate
import ROOT

# Histogram initialization
f = ROOT.TFile("histos-Pie.root", "recreate")
h0 = ROOT.TH1D("h0","h0; Successes",200,264.25,364.25)
h1 = ROOT.TH1D("h1","h1; Pi Estimate",400,2.6,3.6)
h2 = ROOT.TH1D("h2","h2; Normalized Deviation",200,-5.0,5.0)

# 10,000 repetitions of the experiment with different seeds
N = 400
for i in range(10000):
    SEED = 200 + i
    e = PiEstimate(SEED, N)
    h0.Fill(e.nsuccesses)
    h1.Fill(e.estimate)
    ndev = (e.estimate - math.pi)/e.error
    h2.Fill(ndev)

h0.Draw()
h1.Draw()
h2.Draw()
f.Write()
