import numpy as np

'''
np.delete(arr, index, axis=None)
'''

arr =np.array([10,20,30,40])
new_arr = np.delete(arr, 0)
print(new_arr)

arr_2d = np.array([[1,2,3], [4,5,6]])
new_arr_2d = np.delete(arr_2d, 0 , axis=0)
print(new_arr_2d)