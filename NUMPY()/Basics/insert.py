import numpy as np

'''
np.insert(arr, index, value, axis=None)
axis = 1 column wise
axis = 0 row wise
'''
arr = np.array([1,2,3,4,5,6])
new_arr = np.insert(arr, 2, 5, axis=None)
print(new_arr)

arr_2d = np.array([[1,2], [3,4]])
new_arr_2d = np.insert(arr_2d, 1 , [5,6], axis=0)
print(new_arr_2d)