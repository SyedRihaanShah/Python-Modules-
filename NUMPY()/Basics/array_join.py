import numpy as np

arr1 = np.array([[1,2,3],
                  [9,10,12]])
arr2 = np.array([[4,5,6],
                  [2,3,4]])

arr = np.concatenate((arr1, arr2), axis=0)# axis = 0 means vertial/ below one another
#axis = 1 means horizontal or side by side 
#axis = None means as a flat array including all emelemts 
print(arr)

arr3 = np.stack((arr1,arr2))
print(arr3)

arr4 = np.vstack((arr1,arr2))
print(arr4)

arr5 = np.hstack((arr1,arr2))
print(arr5)

arr6 = np.dstack((arr1,arr2))
print(arr6)