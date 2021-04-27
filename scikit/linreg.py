#!/usr/bin/env python3
"""
https://scikit-learn.org/stable/modules/linear_model.html
"""

from sklearn import linear_model

data = ([[0, 0], [1, 1], [2, 2]], [0, 1, 2])

reg = linear_model.LinearRegression()
#reg.fit(data)

reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])