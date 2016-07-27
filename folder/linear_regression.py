##Basic Linear Regression model to find stock market predictors

import pandas as pd
import quandl, math, datetime
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style

# style.use('gggplot')

def get_data():
	df = quandl.get('WIKI/GOOGL')
	df=df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume',]]
	df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
	df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
	df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
	return df
def generate_features(): 
	df = get_data()
	forecast_col = 'Adj. Close'
	df.fillna(-99999, inplace=True)
	##math.ceil takes input, rounds up to 1, returns float. We want to predict 10% of df
	forecast_out=int(math.ceil(0.01*len(df)))
	##label column for each row will be adjusted Close(forecast column) 10 days into future
	##shifting columns negatively
	df['label'] = df[forecast_col].shift(-forecast_out)
	return df, forecast_out
def get_x_and_y():
	df, forecast_out= generate_features()
	X = np.array(df.drop(['label'], 1))
	X = preprocessing.scale(X)
	X = X[:-forecast_out]
	df.dropna(inplace=True)
	y = np.array(df['label'])
	X_lately = X[-forecast_out:]
	y=np.array(df['label'])
	print(len(X), len(y))
	X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
	# clf = LinearRegression(n_jobs=1)
	clf=svm.SVR()
	clf.fit(X_train, y_train)
	accuracy = clf.score(X_test, y_test)
	print ("the accuracy score is {}".format(accuracy))
	##LR is approximately 0.96
	##SVM is approximately 0.79

	#now, predict based on X data. 
	# forecast_set=clf.predict(X_lately)
	# print(forecast_set, accuracy, forecast_out)
get_x_and_y()