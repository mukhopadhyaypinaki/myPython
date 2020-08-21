from __future__ import absolute_import, division, print_function, unicode_literals
#import numpy as np
import pandas as pd
import tensorflow as tf
#import matplotlib.pyplot as plt
#from six.moves import urllib
#import tensorflow.compat.v2.feature_column as fc
import os
def clear(): return os.system('cls')


# Training dataset
dftrain = pd.read_csv(
    'https://storage.googleapis.com/tf-datasets/titanic/train.csv')

# Testing dataset
dfeval = pd.read_csv(
    'https://storage.googleapis.com/tf-datasets/titanic/eval.csv')

# remove survived column form the dataframe as label
y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')

# print(dftrain.loc[0], y_train.loc[0])

CATEGORICAL_COLUMNS = ['sex', 'n_siblings_spouses',
                       'parch', 'class', 'deck', 'embark_town', 'alone']

NUMERICAL_COLUMNS = ['age', 'fare']

feature_columns = []

for feature_name in CATEGORICAL_COLUMNS:
    # gets a list of all unique values from given feature column
    vocabulary = dftrain[feature_name].unique()
    feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(
        feature_name, vocabulary))

for feature_name in NUMERICAL_COLUMNS:
    feature_columns.append(tf.feature_column.numeric_column(
        feature_name, dtype=tf.float32))

# print(feature_columns)


def make_input_fn(data_df, label_df, num_epochs=10, shuffle=True, batch_size=32):
    def input_function():
        ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))
        if shuffle:
            ds = ds.shuffle(1000)
        ds = ds.batch(batch_size).repeat(num_epochs)
        return ds
    return input_function


train_input_fn = make_input_fn(dftrain, y_train)
eval_input_fn = make_input_fn(dfeval, y_eval, num_epochs=1, shuffle=False)


linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns)

linear_est.train(train_input_fn)

eval_result = linear_est.evaluate(eval_input_fn)

clear()

# print(result['accuracy'])

# print(result)

# do perdict

predict_result = list(linear_est.predict(eval_input_fn))
position = 3
print(dfeval.loc[position])
print(y_eval.loc[position])
print(predict_result[position]['probabilities'][1])
