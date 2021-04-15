#!/usr/bin/env python3

"""
KNeighborsClassifier, which creates the edges and the classifier based on 
    the distances
NearestNeighbors, which just calculates the distances
Iris is sample dataset
"""

print(__doc__)

import numpy as np

from sklearn import neighbors
from sklearn import datasets

# Presets
n_neighbors = 15
iris = datasets.load_iris()

kclassifier = KNeighborsClassifier(n_neighbors=3).fit()
nnclassifier = NearestNeighbors().fit()

