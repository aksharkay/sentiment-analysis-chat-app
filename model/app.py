import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import sklearn
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd

app = Flask(__name__)
loaded_vectorizer = pickle.load(open('vectorizer.pickle', 'rb'))
loaded_model = pickle.load(open('classification.model', 'rb'))

@app.route('/predict', methods=['GET'])
def predict():
    text = request.args.get('text')
    transformer = TfidfTransformer(norm='l2', sublinear_tf=True)
    x_test_counts_predict = loaded_vectorizer.transform(text.split())
    transformer.fit(x_test_counts_predict)
    x_test_tfidf_predict = transformer.transform(x_test_counts_predict)
    predictions = loaded_model.predict(x_test_tfidf_predict)
    neg=sum(predictions)/predictions.shape[0]
    print(predictions)
    print(neg)
    return format(neg)

if __name__ == "__main__":
    app.run(debug=True)