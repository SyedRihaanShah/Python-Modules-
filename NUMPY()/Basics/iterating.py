import numpy as np

arr_3d = np.array([[[1,2,3], [4,5,6], [7,8,9]]])
for x in arr_3d:
    for y in x:
        for z in y:
            print(z)

#or we can use nditer()
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']): #we pass opdtypes to convert the data type and flags to 
#make a place for converted data type
  print(x)

for y in np.nditer(arr[:, :, ::2]):
    print(y)

#ndenumerate()
for index,i in np.ndenumerate(arr):
    print(i, index)
    