# Summary.py
import math

def summary(N, NTRIES, SEED, gsum, ggsum, gtrue):
    
# Calculate post-generation statistics
    samplemeang = gsum/float(N)
    samplemeangg = ggsum/float(N)
    besselfactor = float(N)/float(N-1)
    samplevariance = besselfactor*(samplemeangg - samplemeang*samplemeang)
    samplesd = math.sqrt(samplevariance)

# Summary
    print(' ')
    print('Summary based on',N,'samples using SEED',SEED)
    print('Observed mean ',samplemeang)
    print('Observed rms and variance',samplesd, samplesd**2)
    print('RESULT <g> = ',samplemeang,' +- ',samplesd/math.sqrt(N))
    print('Acceptance efficiency ',N/NTRIES)

    gmean = samplemeang
    dgmean = samplesd/math.sqrt(N)
    z = (gmean - gtrue)/dgmean
    print('Correct result = ',gtrue)
    print('Normalized deviation, z = ',z,' standard deviations')
