#!/usr/bin/env python3

import numpy as np

from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestNeighbors

kclassifier = KNeighborsClassifier(n_neighbors=3).fit()
nnclassifier = NearestNeighbors().fit()

