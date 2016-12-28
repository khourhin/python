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
# Make counts for histograms for example
a = data['species'].value_counts()

data.plot()
plt.show()
a.plot(kind='bar')
plt.show()
data.plot.scatter(x='sepal_width', y='sepal_length')
plt.show()

