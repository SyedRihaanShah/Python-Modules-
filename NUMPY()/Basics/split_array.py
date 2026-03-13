import numpy as np

arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr, 3)# we pass two argv one is arr other one is how many parts
#if the given step is smaller at the end it would adjust automatically
print(newarr[0])#returns a list 

#We also have the method split() available but it will not adjust the elements when elements are less
# in source array for splitting like in example above, array_split() worked properly but split() would fail.


arr_2d = np.array([[1,2], [3,4], [5,6], [7,8]])
new_arr_2d = np.array_split(arr_2d,2)
print(new_arr_2d)

arr_2 = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])
new_arr_2 = np.array_split(arr_2, 3, axis=1)
print(new_arr_2)