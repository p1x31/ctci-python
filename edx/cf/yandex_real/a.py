import sys
import numpy as np
import random
import math

from scipy.optimize import minimize

p = np.loadtxt(sys.stdin, dtype=[('x', 'float'), ('y', 'float')], ndmin=1)
x = p['x']
y = p['y']


def f(w, x, y):
    return ((((w[0]+random.uniform(-0.001, 0.001)) * np.exp(x) + (w[1]+random.uniform(-0.001, 0.001)) * (x) ** (3/4)) ** 2 + (w[2]+random.uniform(-0.001, 0.001)) * (np.cos(x) ** 2) - y) ** 2).sum()


res = minimize(f, [1, 1, 1], (x, y), method='Nelder-Mead')
print(*res.x)