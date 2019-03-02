from pandas import Series, DataFrame

import pandas as pd

import numpy as np

import os

import matplotlib.pylab as plt

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

import sklearn.metrics

raw_data = pd.read_csv("./storage/history.csv")
raw_data.dtypes

raw_data.head()

cleaned_data = raw_data.drop("CUST_ID", axis=1)

cleaned_data.corr()['CLV']



predictors = cleaned_data.drop("CLV", axis=1)


targets = cleaned_data.CLV

pred_train, pred_test, tar_train, tar_test = train_test_split(predictors, targets, test_size=.1)

print("Predictor — Training : ", pred_train.shape, "Predictor — Testing : ", pred_test.shape)

model = LinearRegression()

model.fit(pred_train, tar_train)

print("Coefficients: \n", model.coef_)

print("Intercept:", model.intercept_)

# Test on testing data

predictions = model.predict(pred_test)

predictions

sklearn.metrics.r2_score(tar_test, predictions)




new_data = np.array([100,0,50,0,0,0]).reshape(1, -1)

new_pred=model.predict(new_data)

print("The CLV for the new customer is : $",new_pred[0])
