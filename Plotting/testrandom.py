#
# Simple python program using PyROOT to play with random numbers 
# (PyROOT is a python interface to the C++-based ROOT)
#
# TRandom3 is based on the Mersenne twister algorithm and is much faster 
# http://en.wikipedia.org/wiki/Mersenne_twister
#
# See http://root.cern.ch/root/htmldoc/TRandom.html 
# for more details on TRandom class
#
# I am not recommending you go the ROOT/PyROOT direction - although 
# for some of you it may be a possibility to consider.
# I chose ROOT/PyROOT for these illustrations 
# as it is a relatively light way for me 
# to illustrate by doing some of the relevant techniques while 
# relatively conveniently getting access to plots.
# 
#               Graham W. Wilson  
#               updated              27-AUG-2019
#               update to Python3    17-JAN-2022
#
import ROOT
import math

#Check ROOT version
print('ROOT version',ROOT.__version__)    #Does not work for some reason on PHSX-LLxx cluster

twopie = 8.0*math.atan(1.0)

# Initialize output histogram file
f = ROOT.TFile("histos-random.root", "recreate");

# Book histograms
h1 = ROOT.TH1D("h1","h1",100,0.0,1.0)
h2 = ROOT.TH1D("h2","h2",100,0.0,1.0)
hexp = ROOT.TH1D("hexp","hexp",100,0.0,100.0)
hexp2 = ROOT.TH1D("hexp2","hexp2",100,0.0,100.0)
hray = ROOT.TH1D("hray","Rayleigh distribution;r;Entries per 0.05 bin",100,0.0,5.0)
hgau = ROOT.TH1D("hgau","hgau",100,-10.0,10.0)
hgaud = ROOT.TH1D("hgaud","hgaud",100,-10.0,10.0)
hgau2 = ROOT.TH2D("hgau2","hgau2",50,-5.0,5.0,50,-5.0,5.0)
huni2 = ROOT.TH2D("huni2","huni2",50,0.0,1.0,50,0.0,1.0)

# Initialize two independent random number generators 
# using the TRandom1 generator (Ranlux)
# (first argument is the seed), second is the luxury level)
rg1 = ROOT.TRandom1(4538,4)
rg2 = ROOT.TRandom1(4359,4)

# Initalize two independent random number generators using 
# TRandom3 (Mersenne Twister)
#rg1 = ROOT.TRandom3(4538)
#rg2 = ROOT.TRandom3(4359)

for i in range(10000):
# Generate and check distributions of two uniform random numbers, u ~ Un(0,1)
    u1 = rg1.Rndm()
    u2 = rg2.Rndm()
# Note u1 and u2 should be independent
    h1.Fill(u1)
    h2.Fill(u2)
    huni2.Fill(u1,u2)

# Illustrate transformation method to produce random variates

# For exponential distribution   (See Press 7.3.1)
    TAU = 12.0
    hexp.Fill(-TAU*math.log(u1))
    hexp2.Fill(-TAU*math.log(1.0-u1))  #the formula we derived  

# For Rayleigh distribution      (See Press 7.3.5)
    r = float(math.sqrt(-2.0*math.log(u1)))
    hray.Fill(r)

# For Gaussian distribution      (See Press 7.3.4)
# Use r from above. 
# Use the second uniform random number to calculate phi
    phi = twopie*u2
# Now calculate two independent standardized gaussian (normal) variates
    gauss1 = r*math.cos(phi)
    gauss2 = r*math.sin(phi)
    hgau.Fill(gauss1)
    hgau.Fill(gauss2)
    hgaud.Fill(gauss2-gauss1)
    hgau2.Fill(gauss1,gauss2)

# Check values for first 10 i values (iterations 0 to 9)
    if(i<10):
        print(i,u1,u2,r,gauss1,gauss2)

# End of loop

# Create drawing canvas
c1 = ROOT.TCanvas("c1","c1",1200,800);
# Draw the histograms and save to pdf files
h1.Draw()
gchoice=".png"    # could be also eg ".pdf"
c1.Print("h1"+gchoice)
h2.Draw()
c1.Print("h2"+gchoice)
hexp.Draw()
c1.Print("hexp"+gchoice)
hexp2.Draw()
c1.Print("hexp2"+gchoice)
hray.Draw()
c1.Print("hray"+gchoice)
hgau.Draw()
c1.Print("hgau"+gchoice)
hgaud.Draw()
c1.Print("hgaud"+gchoice)
hgau2.Draw()
c1.Print("hgau2"+gchoice)
huni2.Draw()
c1.Print("huni2"+gchoice)

# Save the histograms to a file for potential 
# later inspection directly in ROOT
f.Write()
