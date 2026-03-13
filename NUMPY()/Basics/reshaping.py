import numpy as np 

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_arr = arr.reshape(2,3,2)
print(new_arr)

#unknown dimension
arr_new = arr.reshape(2,2,-1)# -1 is the unknown dimension it automaticaaly assigns the number of elements to adjust
print(arr_new)