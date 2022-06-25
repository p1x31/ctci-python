import sklearn.linear_model as lm
from sklearn.linear_model import Ridge
from sklearn.linear_model import SGDRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from scipy import stats
import numpy as np
import math
import random

x = []
y = []

for line in open('data.txt'):
    xx, yy = map(float, line.strip().split())
    x.append(xx)
    y.append(yy)

features = []
for xx in x:
    curFeatures = [
        math.exp((xx)*2),                          # a^2
        (xx) ** (3/2),                             # b^2
        math.exp(xx) * ((xx) ** (3/4)),            # 2ab
        math.cos(xx) ** 2                          # c
    ]
    features.append(curFeatures)

linearModel = lm.LinearRegression(fit_intercept=True)
#linearModel = lm.Lasso(alpha = 1.0)
#reg = make_pipeline(StandardScaler(), SGDRegressor(max_iter=1000, tol=1e-3))
#linearModel = lm.Ridge(alpha=2.0,tol=1e-3, solver = 'cholesky', random_state=1)
#linearModel = lm.RidgeCV()
#linearModel = lm.SGDRegressor(max_iter=1000, tol=1e-3)
#linearModel = lm.BayesianRidge()
#rf = RandomForestClassifier(n_estimators=100, max_depth=20, random_state=42)
#linearModel = rf
#linearModel = lm.ElasticNetCV()
#linearModel = lm.ElasticNet(max_iter=1000000, selection = 'random')
#linearModel = MLPRegressor()
#epsilon_values = [1.35, 1.5, 1.75, 1.9]
#linearModel = lm.HuberRegressor(alpha=0.000000001, epsilon=1, fit_intercept = False)
linearModel.fit(features, y)
print(linearModel.score(features, y))

#beta_hat = np.linalg.lstsq(features, y, rcond=None)[0]
#print(beta_hat)
#a = math.sqrt(beta_hat[0])
#b = math.sqrt(beta_hat[1])
#c = beta_hat[3]

#print ("free coeff: ", linearModel.intercept_)
#print ("2ab error: ", beta_hat[2] - 2 * a * b)
#print (a, b, c)
#print(np.dot(features,beta_hat))
#x = np.linspace(min(features), max(features), 7)


#from sklearn import preprocessing
#X = preprocessing.StandardScaler().fit(features).transform(features)
#linearModel.fit(X, y)
coeffs = linearModel.coef_
#random.uniform(-0.001, 0.001)
a = math.sqrt(coeffs[0])
b = math.sqrt(coeffs[1])
c = coeffs[3]

print ("free coeff: ", linearModel.intercept_)
print ("2ab error: ", coeffs[2] - 2 * a * b)
print (a, b, c)