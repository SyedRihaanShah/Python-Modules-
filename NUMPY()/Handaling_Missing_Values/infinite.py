import numpy as np

'''
np.isinf()
checks if a num in arr is infinity
'''

arr = np.array([1,2,3,np.inf, 5])
print(np.isinf(arr))

cleaned_arr = np.nan_to_num(arr, posinf=100)
print(cleaned_arr)