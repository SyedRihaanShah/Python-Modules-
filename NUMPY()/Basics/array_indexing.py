import numpy as np

arr_1 = np.array([1,2,3,4,5])
print(arr_1[1])
print(arr_1[-1])

arr_2 = np.array([[1,2,3], [4,5,6]])
print(arr_2[0, 2]) # prints 3 rd element of 1 st row 
print(arr_2[0,-1])

arr_3 = np.array([[[1,2,3,4], [5,6,7,8]],[[9,10,11,12], [13,14,15,16]]])
print(arr_3[0,1,2]) # --> gives 7
print(arr_3[0,1,-1])