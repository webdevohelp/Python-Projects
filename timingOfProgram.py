def func_one(n):
    return [str(num) for num in range(n)]

# print(func_one(10))
print()
def func_two(n):
    return list(map(str,range(n)))
# print(func_two(10))
import time

start_time = time.time()

result = func_one(100000)
end_time = time.time()
es_time = end_time-start_time
print(es_time)
print("\n")
start_time = time.time()

result = func_two(100000)
end_time = time.time()
es_time = end_time-start_time
print(es_time)


import timeit
stmt = '''
func_one(100)
'''
setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

print(timeit.timeit(stmt,setup,number = 10000))

stmt2 = '''
func_two(100)
'''
setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''
print(timeit.timeit(stmt2,setup2,number = 10000))
