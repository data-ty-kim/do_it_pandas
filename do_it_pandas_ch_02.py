#%%
import pandas as pd

df = pd.read_csv('./data/gapminder.tsv', sep='\t')

#%% 02-1
print(df.head())
print(type(df))
print(df.shape)     # size of rows and columns
print(df.columns)
print(df.dtypes)
print(df.info())

#%% 02-2
country_df = df['country']
print(type(country_df))
print(country_df.head())
print(country_df.tail())

subset = df[['country', 'continent', 'year']]
print(type(subset))
print(subset.head())
print(subset.tail())

#%% "loc" method - index
print(df.loc[0])
print(df.loc[99])
print(df.loc[df.shape[0]-1])
print(df.tail(n=1))
print(df.loc[[0, 99, 999]])

#%% "iloc" method - row number
print(df.iloc[1])
print(df.iloc[99])
print(df.iloc[-1])
print(df.iloc[[0, 99, 999]])

#%% slicing - loc
subset = df.loc[:, ['year', 'pop']]
print(subset.head())

#%% slicing - iloc
subset = df.iloc[:, [2, 4, -1]]
print(subset)

#%% range - 1
small_range = list(range(5))
subset = df.iloc[:, small_range]
print(subset)

#%% range - 2
small_range = list(range(3, 6))
subset = df.iloc[:, small_range]
print(subset.head())
#%%
print(df.loc[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']])

# %%
print(df.loc[10:15, ['country', 'lifeExp', 'gdpPercap']])


#%% 02-3
print(df.groupby('year')['lifeExp'].mean())
# %%
multi_group_var = df.groupby(
    ['year', 'continent'])[['lifeExp', 'gdpPercap']].mean()
print(multi_group_var)

# %% return frequency
print(df.groupby('continent')['country'].nunique())

# %%
import matplotlib.pyplot as plt

global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)

# %%
global_yearly_life_expectancy.plot()
