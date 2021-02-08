"""Difference between List and Dictionary in Python
List:
Lists are just like the arrays, declared in other languages.
Lists need not be homogeneous always which makes it a most powerful tool in Python.
A single list may contain DataTypes like Integers, Strings, as well as Objects.
Lists are mutable, and hence, they can be altered even after their creation.



Dictionary:
Dictionary in Python is an unordered collection of data values, used to store data values like a map,
which unlike other Data Types that hold only single value as an element,
Dictionary holds key:value pair.

Key-value is provided in the dictionary to make it more optimized.
Each key-value pair in a Dictionary is separated by a colon :,
whereas each key is separated by a ‘comma’.
"""

Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}  
print("Dictionary with the use of Integer Keys: ")  
print(Dict)
Dict2 = {'Name': 'Geeks', 1: [1, 2, 3, 4]}  
print("\nDictionary with the use of Mixed Keys: ")  
print(Dict2)

print(Dict2[1])

print(Dict2["Name"])