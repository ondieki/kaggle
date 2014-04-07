import csv
import collections
import sys
import numpy
import sklearn
import cPickle as pickle
from sklearn.datasets import load_svmlight_file

def save_object(obj, filename):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

X,Y = load_svmlight_file("space_rm.csv", multilabel=True)
save_object(X, 'trainX.pk1')
save_object(Y, 'trainY.pk1')
