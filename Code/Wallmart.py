import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix

x = pd.read_csv('https://raw.githubusercontent.com/sandeepkhadegenpact/Walmart-Recruiting-II-Sales-in-Stormy-Weather/master/Data/train_logistic.csv',usecols=['tmax', 'tmin','tavg','wetbulb','heat','cool','sealevel','station_number','store_nbr','item_nbr','stnpressure','resultspeed','sunrise', 'sunset','depart', 'dewpoint']);
y = pd.read_csv('https://raw.githubusercontent.com/sandeepkhadegenpact/Walmart-Recruiting-II-Sales-in-Stormy-Weather/master/Data/train_logistic.csv',usecols=['units'])
y['units'] = np.log(y.units+1)

X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=0)
xMatrix = X_train.as_matrix()
yMatrix = y_train.as_matrix()
regr = linear_model.LinearRegression()
regr.fit(xMatrix, yMatrix)

x_predict = X_test;
print(x_predict)

y_predict = regr.predict(x_predict)
print(y_predict)

print('Accuracy of Linear Regression - Data set: {:.2f}'.format(regr.score(X_test, y_test)))
