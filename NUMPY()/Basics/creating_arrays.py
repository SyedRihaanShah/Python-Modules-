import numpy as np
#To create an ndarray, we can pass a 
# list, tuple or any array-like object into the array() method, and it will be converted into an ndarray

arr = np.array((1,2,3,4,5))
print(arr, type(arr))

#Dimensions in array
#nested arrays = arrays which have arrays as elements 

arr_0 = np.array(45) # 0 dimensional array
print(arr_0)
print(arr_0.ndim)

arr_1 = np.array([1,2,3,4])# 1 dimensional array
print(arr_1)
print(arr_1.ndim)

# A tensor is simply a generalization of numbers, vectors, and matrices into higher dimensions. 

arr_2 = np.array([[1,2,3], [4,5,6]])# 2 dimensional array
print(arr_2)
print(arr_2.ndim)

arr_3 = np.array([[[1,2,3], [4,5,6]], [[7,8,9],[10,11,12]]]) # 3 Dimensional array
print(arr_3)
print(arr_3.ndim) #prints number of dimesnions 

#higher dimensional arrays
arr_n = np.array([1,2,3,4], ndmin=5)
print(arr_n)
print(arr_n.ndim)