import numpy as np

arr_1 = np.array([1,2,3,4,5])
print(arr_1[1:2])
print(arr_1[:4])
print(arr_1[1:4:2])

arr_2 = np.array([[1,2,3,4], [5,6,7,8]])
print(arr_2[1,1:3])
print(arr_2[0:2, 2])#from both elements returns index 2
print(arr_2[0:2, 1:2])