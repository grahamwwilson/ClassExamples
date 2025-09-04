# Modify UniformPlot.py
import random
import math
import matplotlib.pyplot as plot
import numpy as np
import subprocess

# Illustrate standard uniform random number generator

# Initialize the random number generator using specified seed
SEED = 208
random.seed(SEED)

NINSTANCES = 1000000        # Number of random numbers to generate

p0 = 0.99

ulist=[]
usum = 0.0
uusum = 0.0

# Generate random numbers, x, in the range [0,1] according to the 
# pdf: p(x) = p0 + 2(1-p0)x with the restriction that
# 0 <= p0 <= 1.0 so that the pdf is non-negative for all x 
# and is properly normalized.

for i in range(NINSTANCES):
    u = random.random() # standard uniform random numbers 
                        # in range [0.0,1.0)
# Use the inverse of the cdf trick
# Here F(x) = p0 x + (1-p0) x**2.
# So write F(x) = u, namely (1-p0) x**2 + p0 x - u = 0.
# Leading to a quadratic whose positive root is a random variable x 
# distributed as r
    if p0 == 1.0:
        x = u
    else:
        x = ( -p0 + np.sqrt(p0**2 + 4.0*(1.0-p0)*u) ) / (2.0*(1.0-p0))
    usum += x
    uusum += x*x
    ulist.append(x)
    if i <= 10:
        print('generated random number',i,'x =',x)

# Calculate post-generation statistics
samplemeanu = usum/float(NINSTANCES)
samplemeanuu = uusum/float(NINSTANCES)
besselfactor = float(NINSTANCES)/float(NINSTANCES-1)
samplevariance = besselfactor*(samplemeanuu - samplemeanu*samplemeanu)
samplesd = math.sqrt(samplevariance)

# Summary
print(' ')
print('Summary based on',NINSTANCES,'instances using SEED',SEED)
print('Observed mean ',samplemeanu)
print('Observed rms ',samplesd)
print('RESULT <x> = ',samplemeanu,' +- ',samplesd/math.sqrt(NINSTANCES))
samplemeanuncertainty = samplesd/math.sqrt(NINSTANCES)
normalizedDeviation = (samplemeanu - 0.5)/samplemeanuncertainty
print('normalizedDeviation = ',normalizedDeviation)

# Print the data

# Plot the generated data in 10 bins 
# Example: 10 equal-width bins from 0.0 to 1.0
bin_edges = np.linspace(0.0, 1.0, 11)
counts, binedges = plot.hist(ulist, bins=bin_edges)[:2]
print('binedges: ',binedges)
print('counts:   ',counts)
plot.title('Distribution Histogram')
plot.xlabel('u')
plot.ylabel('Instances per bin')

# Accumulate a chi-squared quantity using the the first N-1 bins
expected = NINSTANCES//10   # Do exact division to an integer
sd = np.sqrt(expected)
chisq = 0.0
for i in range(len(counts)):
    dev = counts[i] - expected
    chisqcontribution  = ( dev/sd )**2
    chisq += chisqcontribution
    print(f"i = {i:2d}  "
          f"Observed: {counts[i]:8.0f}" 
          f" Expected: {expected:7d}  "
          f"Deviation: {dev:8.0f}  "
          f"Normalized deviation squared: {chisqcontribution:.4f}")
print("Chisq total:",round(chisq, 6))
ndof = len(counts) - 1        # Need to subtract 1 given this is multinomial with the Sum(ni) = N constraint

# Now invoke my pvalues calculator 
# Build the command as a list of strings
cmd = ["python", "../PValues/pvalue.py", "-v", str(round(chisq,6)), "-n", str(ndof)]

# Run the command
subprocess.run(cmd, check=True)

plot.show()

