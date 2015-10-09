import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
%matplotlib inline
sns.set_style("darkgrid")
sns.set_context("notebook")
pd.set_option('precision', 3)

def efficiency(mu):
    return 1.0/(1.0 + mu)

x = np.linspace(0, 3, 100)
rates = [10.0**6, 2*10**6, 4*10**6, 6*10**6, 8*10**6, 10**7]
mus = map(lambda rate: rate * 200 * 10**-9, rates)
efficiencies = map(efficiency, mus)

plt.plot(x, efficiency(x));
plt.scatter(mus, efficiencies, s=50, lw=2, marker='x')
plt.xlim([0, 3])
plt.ylim([0, 1])
plt.ylabel('efficiency');
plt.xlabel('particles per dead time');
pd.DataFrame.from_items([('rate', rates), ('mu', mus), ('efficiency', efficiencies)])
