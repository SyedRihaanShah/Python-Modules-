from numpy import random
import numpy as np

#shuffle
arr = np.array([1,2,3])
random.shuffle(arr)
print(arr)
#shuffle makes changes to orignal arr 
print(random.permutation(arr))#this method returns a re arranged arr 
    