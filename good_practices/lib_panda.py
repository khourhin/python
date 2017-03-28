"""
A lib for data analysis.
See http://pandas.pydata.org/index.html
"""

import pandas as pd
import matplotlib.pyplot as plt

#table = pd.DataFrame([[1,2,3],[4,5,6]], index=['row1','row2'], columns=['col1', 'col2', 'col3'])

# Get quick dataframe to work with:
from bokeh.sampledata.iris import flowers
#print(flowers)

# Read dataframe from csv file
data = pd.read_csv('demo_data/iris.csv')
print(data.head())

# Select by columns
# With names
print(data.sepal_width.head())
# Without names
print(data[[1]].head())
# Make c1ounts for histograms for example
a = data['species'].value_counts()

data.plot()
plt.show()
a.plot(kind='bar')
plt.show()
data.plot.scatter(x='sepal_width', y='sepal_length')
plt.show()

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

flowers.groupby('species').mean().plot(kind='bar')
plt.show()

def listsum(l):
    return  [sum(i) for i in zip(*l)]


# Subset tables

# Check http://nbviewer.jupyter.org/github/jvns/pandas-cookbook/blob/v0.1/cookbook/Chapter%202%20-%20Selecting%20data%20&%20finding%20the%20most%20common%20complaint%20type.ipynb

# df[['colname1','colname2']]

# Filter according to values for ex:
# d[d.fposition > 0]
# d[d.fposition > 0].flength

# Filter by index
SRRs =['SRR2028247','SRR2029611','SRR2029614','SRR2029615','SRR2029617','SRR2029618','SRR2029620','SRR2029621','SRR2029626']

print(df.filter(SRRs, axis=0))

# Filter by regex
df.filter(regex='test')

# And check loc/iloc for subsetting
# df.loc[:,:]

# Build dataframes
## The equivalent of rbind
#df.append(pds.DataFrame(XXXXXXXXXXXX))

# Merge tables
# Check concat, merge etc...

# Change the index of a df
# df.setindex('nameofcolum')
# Or direclty with read_csv(index_col=NUM)
# And select columns directly with usecols in read_csv

# Reorder index
# Check reindex

# Reshaping
# df.transpose()

# Replace NaN
# df.fillna(WHATEVER)

# pivot is the opposite of melt !!! Good for pairwise pmatrix construction

