#Difference Between Lists and Tuples:
#lists are mutable while tuples are immutable.
# A list has a variable size while a tuple has a fixed size.
#The syntax for creating tuple is the same as the syntax for creating a list except you dont use square brackets.


prices = (1,2,6,3,4,9,6,8)
print(len(prices))
#shows the  length of prices tuple
print(2 in prices)
#To check if any item is in the given tuple
prices[1]=22
#this will show an error because tuple does not support item assignment!