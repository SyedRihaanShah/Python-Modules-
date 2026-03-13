from numpy import random
# A random distribution is a set of random numbers that follow a certain probability density function.
# Probability Density Function: A function that describes a continuous probability. i.e. 
# probability of all values in an array

x = random.choice([1,2,3,4], p=[0,0.3,0.5,0.2], size=(2,3))
print(x)