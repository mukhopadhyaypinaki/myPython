from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from six.moves import urllib
import tensorflow.compat.v2.feature_column as fc

# Training dataset
dftrain = pd.read_csv(
    'https://storage.googleapis.com/tf-datasets/titanic/train.csv')

# Testing dataset
dfeval = pd.read_csv(
    'https://storage.googleapis.com/tf-datasets/titanic/eval.csv')

# remove survived column form the dataframe as label
y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')

#print(dftrain.loc[0], y_train.loc[0])
