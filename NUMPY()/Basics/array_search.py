import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])
x = np.where(arr == 4)
y = np.where(arr%2 == 0)
print(x)
print(y)

#There is a method called searchsorted() which performs a binary search in the array, and returns the index
# where the specified value would be inserted to maintain the search order.
z = np.searchsorted(arr, [10,11,12])            #z = np.searchsorted(arr, 7)
w = np.searchsorted(arr, 7 , side= 'right')
print(z)#by default the given index is towards left
print(w)