# UniformPlot.py
import random
import math
import matplotlib.pyplot as plot
import numpy as np
import subprocess

# Illustrate standard uniform random number generator

# Initialize the random number generator using specified seed
SEED = 202
random.seed(SEED)

NINSTANCES = 1000000        # Number of random numbers to generate

ulist=[]
usum = 0.0
uusum = 0.0

# Generate uniform random numbers
for i in range(NINSTANCES):
    u = random.random() # standard uniform random numbers 
                        # in range [0.0,1.0)
    usum += u
    uusum += u*u
    ulist.append(u)
    if i <= 2:
        print('uniform random number',i,'u =',u)

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
print('RESULT <u> = ',samplemeanu,' +- ',samplesd/math.sqrt(NINSTANCES))
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
plot.title('Uniform Distribution Histogram')
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
          f"Observed: {counts[i]:8.0f}  "
          f" Expected: {expected:7d}  "
          f"Deviation: {dev:8.0f}  "
          f"Normalized deviation squared: {chisqcontribution:.4f}")
print("Chisq total:",round(chisq,6))
ndof = len(counts) - 1        # Need to subtract 1 given this is multinomial with the Sum(ni) = N constraint

# Now invoke my pvalues calculator 
# Build the command as a list of strings
cmd = ["python", "../PValues/pvalue.py", "-v", str(round(chisq,6)), "-n", str(ndof)]

# Run the command
subprocess.run(cmd, check=True)

plot.show()


