import numpy as np

arr = np.array([1,7,4,2])
arr_2d = np.array([[1,5,2,7], [9,3,6,2]])

print(np.sort(arr))#this method returns a copy of the sorted array the orignal is unchanged
print(np.sort(arr_2d))