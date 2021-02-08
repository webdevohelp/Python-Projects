#to find the reverse of a list and sort it & make a copy
listt = ['hello','dude','how','are','you','Doing?']

rev_listt = listt.copy()
#making a copy
print(rev_listt)

rev_listt.reverse()
#reversing the list
print(rev_listt)

print("Methods for working with lists:")
print("append() : adds item to the end of list \nclear() : removes all items from the list \n copy() : makes a copy of a list \n count() : counts how many times an element appears in the list!\nextend() : appends the items from one list to the end of other list!\n index() : Returns the index number of an element!\ninsert() : inserts an items into a list\npop() : removes an element from the list from the end of from mentioned position \nremove(): removes one ite from the list \nreverse() : reverses the order of items in a list\nsort() : Sorts the list in ascending order. Put reverse = True inside the parentheses to sort in descending order.")