#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import sklearn
import pickle
from sklearn.feature_extraction.text import TfidfTransformer

loaded_vectorizer = pickle.load(open('vectorizer.pickle', 'rb'))
loaded_model = pickle.load(open('classification.model', 'rb'))

text=input('enter text: ')
transformer = TfidfTransformer(norm='l2', sublinear_tf=True)
x_test_counts_predict = loaded_vectorizer.transform(text.split())
transformer.fit(x_test_counts_predict)
x_test_tfidf_predict = transformer.transform(x_test_counts_predict)
predictions = loaded_model.predict(x_test_tfidf_predict)
print(predictions)
neg=sum(predictions)/predictions.shape[0]
print ("percentage of negetivity: ", neg*100)