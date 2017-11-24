from multiprocessing import Pool


def f(x):
    return x*x

# USING of the partial trick to pass other parameters

if __name__ == '__main__':
    p = Pool(5)
    print(p.map(f, [1, 2, 3]))

