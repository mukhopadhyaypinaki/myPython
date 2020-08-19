import pandas as pd
import tensorflow as tf


dftrain = pd.read_csv(
    'https://storage.googleapis.com/tf-datasets/titanic/train.csv')

dfeval = pd.read_csv(
    'https://storage.googleapis.com/tf-datasets/titanic/eval.csv')

y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')


print(dftrain.info())
