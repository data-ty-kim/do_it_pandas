# %%
###########################
######## CHAPTER 10 #######
###########################
##### Apply Functions #####
###########################

# %%
# import modules
import pandas as pd
import numpy as np
import seaborn as sns

# %% 10-2
# Apply (Basics)
df = pd.DataFrame({'a': [10, 20, 30], 'b': [20, 30, 40]})
print(df)

# %%
# we could have directly squared the column.
print(df['a']**2)

# %%
# Apply Over a Series

def my_sq(x):
    """Square a given value"""
    return x ** 2


# apply our square function on the 'a' column
sq = df['a'].apply(my_sq)
print(sq)

# %%
# writing a function that takes two parameters

def my_exp(x, n):
    return x ** n


# exponent, n, to 2
ex = df['a'].apply(my_exp, n=2)
print(ex)

# exponent, n, to 3
ex = df['a'].apply(my_exp, n=3)
print(ex)

# %%
# Apply Over a DataFrame
# we first need to specify which axis to apply the function over
# for example, column-by-column or row-by-row

# The function below does not have a return statement
# All it is doing is displaying on the screen whatever we pass it
def print_me(x):
    print(x)


# Column-Wise Operations
df.apply(print_me, axis=0)

# %%
# when we use .apply(), the entire column is passed into the first argument

def avg_3_apply(col):
    sum=0
    for item in col:
        sum += item
    return sum / df.shape[0]


print(df.apply(avg_3_apply))

# %%
# Row-Wise Operations
def avg_2_apply(row):
    sum=0
    for item in row:
        sum += item
    return sum / df.shape[1]


print(df.apply(avg_2_apply, axis=1))

# %% 10-3
# Load dataset
titanic = sns.load_dataset("titanic")
print(titanic.info())

# %%
# Apply (Advanced)

def count_missing(vec):
    null_vec = pd.isnull(vec)
    null_count = np.sum(null_vec)
    return null_count


cmis_col = titanic.apply(count_missing)
print(cmis_col)

# %%
def prop_missing(vec):
    num = count_missing(vec)
    dem = vec.size
    return num / dem


pmis_col = titanic.apply(prop_missing)
print(pmis_col)

# %%
# Row: axis=1
cmis_row = titanic.apply(count_missing, axis=1)
print(cmis_row.head())

# %%
titanic['num_missing'] = titanic.apply(count_missing, axis=1)
print(titanic.head())

# %% Vectorized Functions
def avg_2(x,y):
    return (x+y)/2

print(avg_2(df['a'], df['b']))
