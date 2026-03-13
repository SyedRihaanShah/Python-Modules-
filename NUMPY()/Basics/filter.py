import numpy as np

#Getting some elements out of an existing array and creating a new array out of them is called filtering.

arr = np.array([1,2,3,4])

x = [True, False, True, True]
new_arr = arr[x]
print(new_arr)
#creating a filter array
y = np.array([10,15,20,25])
filter_array= []

for num in y :
    if num > 15 :
        filter_array.append(True)
    else:
        filter_array.append(False)

#or 

filter_array_2 = y > 15
filter_array_3 = y % 2 == 0

z = y[filter_array_3]
print(filter_array_2)
print(z)