import math
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LassoCV
from sklearn.metrics import mean_squared_error


def rmsle(y_pred, y_test) : 
    assert len(y_test) == len(y_pred)
    return np.sqrt(np.mean((np.log(1+y_pred) - np.log(1+y_test))**2))


def regression(data):
	data = pd.get_dummies(data)
	x = data.drop('SalePrice', axis=1)
	y = data.SalePrice
	x_train, x_test , y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=1)

	lassocv = LassoCV(alphas=None, cv=5, max_iter=100000, normalize=True)
	lassocv.fit(x_train, y_train)
	alpha = lassocv.alpha_
	y_pred = lassocv.predict(x_test)

	print('alpha: ', alpha)
	print('RMSE: ', math.sqrt(mean_squared_error(y_test, y_pred)))
	print('RMLSE: ', rmsle(y_test, y_pred))

if __name__ == '__main__':
	datafile = 'train.csv'
	data = pd.read_csv(datafile, keep_default_na=False,  na_values=['NA_'])
	data = data.drop('Id', axis=1)

	regression(data)
