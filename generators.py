def genSquares(n):
    for x in range(n):
        yield x**2
x = genSquares(10)
for num in x:
    print(num)

import random
x = int(input("Enter the min number"))
y = int(input("Enter the max number"))
z = int(input("Enter the amount of random numbers you want!"))
def randNum(z):
    for num in range(z):
        yield random.randint(x,y)

randNums = randNum(z)
for nums in randNums:
    print(nums)

x = iter("hello")
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

