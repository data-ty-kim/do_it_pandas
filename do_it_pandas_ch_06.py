# %%
###############
## CHAPTER 6 ##
###############
import pandas as pd
import numpy as np
from numpy import NaN, NAN, nan

# %% 06-1 Missing Value
# below results are all False
print(NaN == True)
print(NaN == False)
print(NaN == 0)
print(NaN == '')
print(NaN == NaN)
print(NaN == nan)
print(NaN == NAN)
print(nan == NAN)

# %%
# to check the missing value
print(pd.isnull(NaN))
print(pd.isnull(nan))
print(pd.isnull(NAN))
print(pd.notnull(NAN))
print(pd.notnull(42))
print(pd.notnull('missing'))

# %%
# load csv to see the example of missing values
ebola = pd.read_csv('./data/country_timeseries.csv')
print(ebola.head())
print(ebola.count())

# %%
# count the number of missing values
num_rows = ebola.shape[0]
num_missing = num_rows - ebola.count()
print(num_missing)

# %%
# use count_nonzero, isnull method
print(np.count_nonzero(ebola.isnull()))
print(np.count_nonzero(ebola['Cases_Guinea'].isnull()))

# %%
# use value_counts method
print(ebola.Cases_Guinea.value_counts(dropna=False).head())

# %%
# how to handle missing values: fillna
# replace
print(ebola.fillna(0).iloc[0:10, 0:5])
# fill forwards
print(ebola.fillna(method='ffill').iloc[0:10, 0:5])
# fill backwards
print(ebola.fillna(method='bfill').iloc[0:10, 0:5])

# %%
# how to handle missing values: interpolate
# to put a middle value between other rows
print(ebola.interpolate().iloc[0:10, 0:5])

# %%
# Drop Missing values
ebola_dropna = ebola.dropna()
print(ebola.shape)
print(ebola_dropna.shape)
print(ebola_dropna)
# If we only keep complete cases in our ebola dataset, 
# we are only left with 1 row of data.

# %%
# Calculations with missing data
# Let’s say we wanted to look at the case counts 
# for multiple regions. We can add multiple regions together 
# to get a new columns of case counts.
ebola['Cases_multiple'] = \
    ebola['Cases_Guinea'] + ebola['Cases_Liberia'] + ebola['Cases_SierraLeone']
ebola_subset = ebola.loc[:, ['Cases_Guinea', 'Cases_Liberia', 'Cases_SierraLeone', 'Cases_multiple']]
print(ebola_subset.head(n=10)) # the first 10 lines of the calculation.

# %%
# calculate a value by skipping over the missing values
print(ebola.Cases_Guinea.sum(skipna=True))
print(ebola.Cases_Guinea.sum(skipna=False))
