import math

value = 4.35

print(math.floor(value))
print(math.ceil(value))
print(round(value))

print(math.pi)
print(math.inf)

print(math.log(math.e))

print(math.log(100,10))
print(math.log(128,2))

print(math.sin(180))

import random
print(random.randint(10,100))
random.seed(101)
print()
print(random.randint(10,100))
print(random.randint(10,100))
print(random.randint(10,100))
print(random.randint(10,100))
print(random.randint(10,100))

print("\n")

mylist = range(0,10)
print(random.choices(population=mylist,k=8))

print(random.choices(population=mylist,k=5))

print(random.gauss(mu=0,sigma=1))