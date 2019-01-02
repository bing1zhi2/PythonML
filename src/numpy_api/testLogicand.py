import numpy as np

predict_issame = np.array([True,False,True])
actual_issame = np.array([False,True,False])
true_accept = np.sum(np.logical_and(predict_issame, actual_issame))
print(true_accept)