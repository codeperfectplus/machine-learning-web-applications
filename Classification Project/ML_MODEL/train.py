#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 21:10:51 2020

@author: codeperfectplus
"""
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

np.random.seed(10)
iris = load_iris()
X = iris.data; y = iris.target

train_X, test_X, train_y, test_y = train_test_split(X, y, 
                                                    train_size=0.8)

clf = RandomForestClassifier(n_estimators=200, criterion ="gini").fit(train_X, train_y)
pred_y = clf.predict(test_X)
score = accuracy_score(test_y, pred_y); print(score)

filename = 'classifier.pkl'

# dump model
joblib.dump(clf, filename)

#load model
#load_model = joblib.load(filename)
