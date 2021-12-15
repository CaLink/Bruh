import pandas as pd

from matplotlib import pylab
import numpy as np


csv = 'Dataset.csv'

# Preparing

#orig = pd.read_csv(csv)
tab = pd.read_csv(csv,index_col="PassengerId")

#Delete all NaN Row
tab = tab.dropna()

# Description

#3
tHead = list(tab.columns)
tType = tab.dtypes

print(tHead)
print(tType)


#4
print(tab.describe())

#5
graph = tab.hist()
print (graph)

x = np.random.randn(10000)
hist(x, 100)

