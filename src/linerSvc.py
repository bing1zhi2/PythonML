# -*- coding:utf-8 -*-
import numpy as np
from sklearn.svm import SVC
import pickle

X = np.array([[-1, -1], [-2, -1],[1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])
clf = SVC(kernel='linear', probability=True)
clf.fit(X, y)
a = [[-0.8, -1]]
pro = clf.predict_proba(a)
print(pro)
class_names =['a', 'b', 'c', 'd']
classifier_filename_exp= "F:/dataset/mydata/model/my_test.pkl"
with open(classifier_filename_exp, 'wb') as outfile:
    pickle.dump((clf,class_names), outfile)
