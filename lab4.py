import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import scale 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso, LassoCV
from sklearn.metrics import mean_squared_error

def rmsle(y_pred, y_test) : 
    assert len(y_test) == len(y_pred)
    return np.sqrt(np.mean((np.log(1+y_pred) - np.log(1+y_test))**2))

def regression(data):
	y = data.SalePrice
	x = data.drop(['SalePrice'], axis=1)
	x_train, x_test , y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=1)

	lasso = Lasso(max_iter=10000, normalize=True)
	lassocv = LassoCV(alphas=None, cv=5, max_iter=100000, normalize=True)
	lassocv.fit(x_train, y_train)
	print('alpha: ', lassocv.alpha_)
	lasso.set_params(alpha=lassocv.alpha_)
	lasso.fit(x_train, y_train)
	print('RMSE: ', math.sqrt(mean_squared_error(y_test, lasso.predict(x_test))))
	print('RMLSE: ', rmsle(y_test, lasso.predict(x_test)))

if __name__ == '__main__':
	datafile = 'train.csv'
	data = pd.read_csv(datafile, keep_default_na=False,  na_values=['NA_'])
	data = data.drop('Id', axis=1)
	data = pd.get_dummies(data)
	
	regression(data)
