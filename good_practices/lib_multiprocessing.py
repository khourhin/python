from multiprocessing import Pool
from functools import partial  # For multiple arguments


def f(x):
    return x * x


# USING of the partial trick to pass other parameters


# To use a class method on a list of objects
from operator import methodcaller

map(methodcaller("methodname"), object_list)

# Or pass by lambda:

map(lambda obj: obj.method(), objectlist)


if __name__ == "__main__":
    p = Pool(5)
    print(p.map(f, [1, 2, 3]))
