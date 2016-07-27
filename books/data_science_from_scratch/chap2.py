# Functionnal tools
from functools import partial


def exp(base, power):
    return base ** power

two_to_the = partial(exp, 2)     # is now a function of one variable
print(two_to_the(3))              # 8
square_of = partial(exp, power=2)
print(square_of(3))               # 9

# Zipping/Unzipping

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zip(list1, list2)        # is [('a', 1), ('b', 2), ('c', 3)]

pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs) # [('a','b','c'), ('1','2','3')].
