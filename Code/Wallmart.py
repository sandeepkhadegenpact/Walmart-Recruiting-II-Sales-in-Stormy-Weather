import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split

data = pd.read_csv('https://raw.githubusercontent.com/sandeepkhadegenpact/Walmart-Recruiting-II-Sales-in-Stormy-Weather/master/Data/train.csv')

data = data.dropna()
print(data.shape)
print(list(data.columns))

data2 = pd.get_dummies(data, columns =['date', 'store_nbr', 'item_nbr', 'units'])
data2.drop(data2.columns[[1, 2]], axis=1, inplace=True)
data2.columns

X = data2.iloc[:,1:]
y = data2.iloc[:,0]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

#Fit logistic regression to the training set
X_train.shape
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)

print('Accuracy of Training/Test Data set: {:.2f}'.format(classifier.score(X_test, y_test)))

# read data from git
# key = pd.read_csv('https://github.com/sandeepkhadegenpact/Walmart-Recruiting-II-Sales-in-Stormy-Weather/blob/master/Data/key.csv')
# wtr = pd.read_csv('https://raw.githubusercontent.com/sandeepkhadegenpact/Walmart-Recruiting-II-Sales-in-Stormy-Weather/master/Data/weather')



