#counter
from collections import Counter

letters = 'aaaabbbbccccddddaacd'
c = Counter(letters)
print(c)
print(c.most_common(4))
print(list(c))

#2 defaultdict
from collections import defaultdict

d = {'a':10}
print(d)
print(d['a'])

d = defaultdict(lambda: 0)
d['correct'] = 100
print(d['wrong'])
print(d)

#namedtuple
from collections import namedtuple
Dog = namedtuple('Dog',['age','breed','name'])
sammy = Dog(age = 5,breed = 'Husky',name = 'Sam')
print(sammy)
print(sammy.age)
print(sammy.breed)
print(sammy.name)