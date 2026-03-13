import numpy as np

arr = np.array([[1,2,3,4], [5,6,7,8]])
print(arr.shape)
#shape returns a tuple with number of elements at each index

arr1 = np.array([1,2,3], ndmin=5)
print(arr1.shape)