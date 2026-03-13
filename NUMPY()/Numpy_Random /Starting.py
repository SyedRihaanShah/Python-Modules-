from numpy import random

x = random.randint(100)#prints a random number from 0 to 100
print(x)
y = random.rand()#gives a float in between 0 and 1 
print(y)    

#to create a random array 
z = random.randint(100, size=5)
w = random.randint(100, size=(2,2,3))
print(w)

#choice is to pick a singl/multiple numbers from a array
a = random.choice([1,2,3,4,5],size=(1,2))
print(a)