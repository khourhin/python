import random
from collections import Counter
import matplotlib.pyplot as plt
import logging as log
import chap4
import math

log.basicConfig(level=log.INFO)

num_friends = ([random.randrange(0, 100) for _ in range(100)])

friends_count = Counter(num_friends)

xs = range(101)
ys = [friends_count[x] for x in xs]

plt.bar(xs, ys)
plt.title('Friends histogram')
plt.xlabel('# of friends')
plt.ylabel('# of people')
plt.show()

# Doing some stats:

def mean(x):
        return sum(x) / len(x)

def median(v):
    """finds the 'middle-most' value of v"""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    
    if n % 2 == 1:
        # if odd, return the middle values
        return sorted_v[midpoint]
    else:
        # if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

    
def quantile(x, p):
    """
    Returns the pth-percentile value in x
    """
    p_index = int(p * len(x))
    return sorted(x)[p_index]


def mode(x):
    """
    Returns a list (might be more than 1 mode)
    """

    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]


def data_range(x):
    return max(x) - min(x)


def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return chap4.sum_of_squares(deviations) / (n - 1)
            

def standard_deviation(x):
    return math.sqrt(variance(x))


def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)


def covariance(x, y):
    n = len(x)
    return chap4.dot(de_mean(x), de_mean(y)) / (n - 1)


def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)

    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / sted_x / sted_y
    else:
        return 0 # if no variation, correlation is zero

stats = {
    'N_Obs': len(num_friends),
    'mean': sum(num_friends) / len(num_friends),
    'median': median(num_friends),
    'max': max(num_friends),
    'min': min(num_friends),
    'quant0.1': quantile(num_friends, 0.1),
    'quant0.25': quantile(num_friends, 0.25),
    'quant0.75': quantile(num_friends, 0.75),
    'quant0.90': quantile(num_friends, 0.90),
    'mode': mode(num_friends),
    'range': data_range(num_friends),
    'variance': variance(num_friends),
    'std dev': standard_deviation(num_friends),
    'interquartile_range': interquartile_range(num_friends),
    'covariance': covariance(num_friends, num_friends),
}

for stat in stats:
    log.info('{0}:{1}'.format(stat, stats[stat]))
