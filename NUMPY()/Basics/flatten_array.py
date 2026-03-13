import numpy as np

'''
flatten -> multi dim arr to 1d arr
.ravel() -> orignal arr is affected
.flatten() -> returns a copy
'''


arr = np.array([[1,2,3], [4,5,6]])
print(arr.ravel())
print(arr.flatten())