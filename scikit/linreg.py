#!/usr/bin/env python3

"""
https://scikit-learn.org/stable/modules/linear_model.html
"""

import numpy as np
from sklearn import linear_model

# Sample data is 1 dimensional with 1 label
# Use this formatting where each sample is a list because a sample can
# contain an arbitrary number of features.
#TODO Is this list of lists how to fake a numpy array?
#TODO take list and reshape it
X = [[0], [1], [2], [3]]
l = [0, 1, 2, 3, 4]
X2 = np.array(l)
print("X2", X2)

# lables are for a line that fits y = 2x + b
y = [-1, 2, 4, 6]


reg = linear_model.LinearRegression()
reg.fit(X, y)

test_data = [[1.2], [10]]

print(reg.predict(test_data))