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

trainX,trainY = load_svmlight_file("space_rm.csv", multilabel=True)
save_object(trainX, 'trainX.pk1')
save_object(trainY, 'trainY.pk1')

testX,blank = load_svmlight_file("test.csv")
save_object(testX, 'testX.pk1')