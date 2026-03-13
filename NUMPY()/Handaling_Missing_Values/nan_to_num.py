import numpy as np
#np.nan_to_num(array, nan=value) default - 0

arr = np.array([1,2,3,np.nan])
cleaned_arr = np.nan_to_num(arr)
print(cleaned_arr)