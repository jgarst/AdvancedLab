import numpy as np
import scipy.stats as st
periods = np.array([1.35, 1.34, 1.32, 1.36, 1.33, 1.34, 1.37, 1.35])

sum = 0
for p in periods: sum += p

mean = sum / len(periods)
print "mean: {0:.4f}".format(mean)

squareDiff = 0
for p in periods: squareDiff += (p - mean)**2

s = np.sqrt(squareDiff/(len(periods) - 1))
print "standard deviation: {0:.4f}".format(s)