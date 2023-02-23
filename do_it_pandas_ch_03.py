# %%
import pandas as pd
from collections import OrderedDict
import random
import os

# %% 03-1 
# to make series
s = pd.Series(['banana', 42])
print(s)

# %%
# to set an index
s = pd.Series(['Wes McKinney', 'Creator of Pandas'], index=['Person', 'Who'])
print(s)

# %%
# to make a dataframe
scientists = pd.DataFrame({
    'Name': ['Rosline Franklin', 'William Gosset'],
    'Occupation': ['Chemist', 'Statistician'],
    'Born': ['1920-07-25', '1876-06-13'],
    'Died': ['1958-04-16', '1937-10-16'],
    'Age': [37, 61]}
    )
print(scientists)

# %%
# to set an index
scientists = pd.DataFrame(
    data={'Occupation': ['Chemist', 'Statistician'],    
          'Born': ['1920-07-25', '1876-06-13'],
          'Died': ['1958-04-16', '1937-10-16'],
          'Age': [37, 61]},
    index=['Rosaline Franklin', 'William Gosset'],
    columns=['Occupation', 'Born', 'Age', 'Died']
)
print(scientists)

# %%
scientists = pd.DataFrame(OrderedDict([
    ('Name', ['Rosaline Franklin', 'William Gosset']),
    ('Occupation', ['Chemist', 'Statistician']),
    ('Born', ['1920-07-25', '1876-06-13']),
    ('Died', ['1958-04-16', '1937-10-16']),
    ('Age', [34, 61])
])
)
print(scientists)

# %% 03-2
scientists = pd.DataFrame(
    data={'Occupation': ['Chemist', 'Statistician'],
          'Born': ['1920-07-25', '1876-06-13'],
          'Died': ['1958-04-16', '1937-10-16'],
          'Age': [37, 61]},
    index=['Rosaline Franklin', 'William Gosset'],
    columns=['Occupation', 'Born', 'Died', 'Age'])

first_row = scientists.loc['William Gosset']
print(type(first_row))
print(first_row)

# %%
# index, values, keys
print(first_row.index)
print(first_row.values)
print(first_row.keys())
print(first_row.index[0])
print(first_row.keys()[0])

# %%
# mean, min, max, std
ages = scientists['Age']
print(ages)
print(ages.mean())
print(ages.min())
print(ages.max())
print(ages.std())

# %%
scientists = pd.read_csv('./data/scientists.csv')
# print(scientists.head())

ages = scientists['Age']
print(ages.max())
print(ages.mean())
print(ages[ages > ages.mean()])
print(ages > ages.mean())

manual_bool_values = [True, True, False, False, True, True, False, True]
print(ages[manual_bool_values])

# %%
# Series and Broadcasting
print(ages + ages)
print(ages * ages)
print(ages +100)
print(ages *2)

# %%
print(ages + pd.Series([1, 100]))

# %%
# reverse the index
rev_ages = ages.sort_index(ascending=False)
print(rev_ages)

print(ages*2 == ages + rev_ages)

# %% 03-4
# dataframe - boolean extract
print(scientists[scientists['Age'] > scientists['Age'].mean()])
print()
print(scientists.loc[scientists['Age'] > scientists['Age'].mean()])
print()
# print(scientists.loc[[True, True, False, True]]) 
# -> Boolean index has wrong length: 4 instead of 8

# %% 03-5
print(scientists.info())

born_datetime = pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
print(born_datetime)

died_datetime = pd.to_datetime(scientists['Died'], format='%Y-%m-%d')
print(died_datetime)

# %%
scientists['born_dt'], scientists['died_dt'] = (born_datetime, died_datetime)
# print(scientists.head())
print(scientists.shape)
scientists.drop(columns=['Born', 'Died'], inplace=True)
scientists['age_days_dt'] = (scientists['died_dt'] - scientists['born_dt'])
print(scientists)

# %%
random.seed(42)
random.shuffle(scientists['Age'])
print(scientists['Age'])

scientists_dropped = scientists.drop(['Age'], axis=1)
print(scientists_dropped.columns)

# %% 03-6
# to save dataframes as a pickle
names = scientists['Name']
os.mkdir("output")
names.to_pickle('./output/scientists_names_series.pickle')
scientists.to_pickle('./output/scientists_df.pickle')

# %%
scientists_from_pickle = pd.read_pickle(
    './output/scientists_df.pickle'
    )

print(scientists_from_pickle)

# %%
# to save as a csv or a tsv
names.to_csv('./output/scientist_names_series.csv')
scientists.to_csv('./output/scientists_df.tsv', sep='\t')
