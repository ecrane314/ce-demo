#!/usr/bin/env python3

"""
April 2021
KNeighborsClassifier, which creates the edges and the classifier based on
    the distances
NearestNeighbors, which just calculates the distances
Iris is sample dataset
Doc https://scikit-learn.org/stable/modules/neighbors.html
Sample https://scikit-learn.org/stable/auto_examples/neighbors/\
plot_classification.html#sphx-glr-auto-examples-neighbors-plot-\
classification-py
"""

#print(__doc__)

import numpy as np

from sklearn import neighbors
from sklearn import datasets

# Presets
N_NEIGHBORS = 15

iris = datasets.load_iris()
x = iris.data[:, :2]
y = iris.target
print(type(iris))
print(type(x))
print(type(y))

kclassifier = neighbors.KNeighborsClassifier(x=x, y=y, n_neighbors).fit()
nnclassifier = neighbors.NearestNeighbors(x).fit()

#TODO Fix so it works
#TODO Fix lint 