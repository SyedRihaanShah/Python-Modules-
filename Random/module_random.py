import random

a = random.random() #returns a floating point number in between 0 and 1 exculding 1 
print(a)

b = random.randint(1,10) # returns a random number in the given range and both ends are exculsive
print(b)

c = random.randrange(1,20,2) # Generates a random number from a given range with an optional step value
print(c) #syntax = random.randrange(start, stop, step)

d = random.uniform(1.3, 4.2) #returns a floating point type in between given range
print(d)

l = ['red', 'blue', 'green', 'orange', 'yellow', 'blue']
e = random.choice(l) #Selects one random element from a list, tuple, or string.
print(e)

f = random.choices(l, k =2) # multiple random elemets can be choosed but they might repeat
print(f)#syntax = random.choices(list,tuple,string; k = 'value)

g = random.sample(l, 3)# same as choices but all choices are random 
print(g) 

num = [1,2,3,4,5]
random.shuffle(num) #shuffles elements in a list
print(num)

random.seed()# useful to get reproducalble results if we put a seed in the bracket
print(random.randint(1,100))

