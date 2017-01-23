"""
A lib for data analysis.
See http://pandas.pydata.org/index.html
"""

import pandas as pd


table = pd.DataFrame([[1,2,3],[4,5,6]], index=['row1','row2'], columns=['col1', 'col2', 'col3'])


# Playing with groupby
a = [[1,0,0], [1,1,0], [1,0,1], [0,1,0], [0,1,0], [0,0,1], [0,0,1]]
b = ['gene1','gene1','gene1','gene2','gene2','gene3','gene3',]
df = pd.DataFrame({'ints':a, 'gene':b})

grouped = df.groupby('gene')

print(grouped.first())
print(grouped.last())

print(grouped.get_group('gene1'))

print(grouped.sum())

print(grouped.size())

print(grouped.describe())


def listsum(l):
    return  [sum(i) for i in zip(*l)]


# Subset tables
# df[['colname1','colname2']]

# Filter according to values for ex:
# d[d.fposition > 0]
# d[d.fposition > 0].flength

# And check loc for subsetting
