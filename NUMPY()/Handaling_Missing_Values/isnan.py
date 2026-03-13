import numpy as np

'''
np.isnan(arr)
nan = not a number 
'''

arr = np.array([1,2, np.nan, 4, np.nan, 6])
print(np.isnan(arr))

print(np.nan == np.nan)#returns False as its not true