import numpy as np

#copy makes a new duplicate array stored in the variable and changes made to the copy arr doesnt affect orgianel arr and vice versa
#copies own data where as view doesnt own data
arr = np.array([1,2,3,4])
x = arr.copy()
arr[0] = 21

print(arr)
print(x)


#view gives the orginal arr to the variable so changes made in origanal arr can be seen in view arr to and vice versa
v_arr = np.array([4,3,2,1])
y = v_arr.view()
v_arr[0] = 23
print(v_arr)
print(y)

#to check if a varaibles owns a data we use base 
print(x.base)
print(y.base)
#returns None if it owns the data