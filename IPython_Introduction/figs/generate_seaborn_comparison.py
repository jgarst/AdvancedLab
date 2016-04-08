#!/bin/python
"""Run first example, change an save it's plot format."""
import nbformat as nbf
import matplotlib
matplotlib.use('svg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as st
from os import chdir

chdir('../notebooks')
notebook = nbf.read('first_example.ipynb', as_version=4)
cells = notebook.cells[1:]
sources = [cell['source'] for cell in cells]
for source in sources:
    exec(source)

chdir('../figs')
fig.savefig('matplotlib_default.svg')

import seaborn as sns
sns.set_context('paper')
chdir('../notebooks')
for source in sources:
    exec(source)

chdir('../figs')
fig.savefig('matplotlib_seaborn.svg')
