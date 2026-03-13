import numpy as np

arr = np.array([1,2,3,4])
print(arr.dtype)

arrname = np.array(['apple', 'banana'], dtype="<U4")#or you can assigin a length of the string 
print(arrname.dtype) # this would give output <U6 which mean unicode string with max lenght 6

arr_fix = np.array([1,2,3,4], dtype='S')
print(arr_fix.dtype)

arr_cus = np.array([1.1,2.1, 4.5])
print(arr_cus.astype('i'))
new_arr = arr_cus.astype(int)
print(new_arr)

bool_arr = np.array([1,0,3])
arr_tru = bool_arr.astype(bool)
print(arr_tru)
'''
i - integer
b - boolean
u - unsigned integer --> only +ve int
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''