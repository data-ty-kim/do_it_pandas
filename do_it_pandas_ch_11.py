# %%
##########################
####### CHAPTER 11 #######
##########################
### Groupby Operations ###
##########################

# %%
# import modules
import pandas as pd
import numpy as np
import seaborn as sns

# %%
# load data
df = pd.read_csv('./data/gapminder.tsv', sep='\t')

# %%
# calculate the average life expectancy for each year
avg_life_exp_by_year = df.groupby('year').lifeExp.mean()
print(avg_life_exp_by_year)

# %%
# how groupby statements work?
# get a list of unique years in the data
years = df.year.unique()
print(years)

# %%
# subset the data for the year 1952
y1952 = df.loc[df.year == 1952, :]
print(y1952)

# %%
# take the mean of the lifeExp values
y1952_mean = y1952.lifeExp.mean()
print(y1952_mean)

# %%
# repeat this process for every year column
y1957 = df.loc[df.year == 1957, :]
y1957_mean = y1957.lifeExp.mean()

y1962 = df.loc[df.year == 1962, :]
y1962_mean = y1962.lifeExp.mean()

y2007 = df.loc[df.year == 2007, :]
y2007_mean = y2007.lifeExp.mean()

df2 = pd.DataFrame({"year": [1952, 1957, 1962, 2007],
                    "": [y1952_mean, y1957_mean, y1962_mean, y2007_mean]})

print(df2)

# %%
# Aggregation Function
# use custom function into agg
def my_mean(values):
    n = len(values)
    sum = 0
    for value in values:
        sum += value
    return sum / n

agg_my_mean = df.groupby('year')["lifeExp"].agg(my_mean)
print(agg_my_mean)

# %%
# functions that take multiple parameters
def my_mean_diff(values, diff_value):
    n = len(values)
    sum = 0
    for value in values:
        sum += value
    mean = sum / n
    return (mean - diff_value)


# calculate the global average life expectancy mean
global_mean = df["lifeExp"].mean()
print(global_mean)

# %%
# custom aggregation function with multiple parameters
agg_mean_diff = (
    df
    .groupby("year")
    ["lifeExp"]
    .agg(my_mean_diff, diff_value=global_mean)
)

print(agg_mean_diff)

# %%
# Multiple Functions simultaneously
# calculate the count, mean, std of the lifeExp by continent
gdf = (
    df
    .groupby("year")
    ["lifeExp"]
    .agg([np.count_nonzero, np.mean, np.std])
)

print(gdf)

# %%
# use a dictionary on a dataframe to agg different columns
# for each year, calculate the 
# average lifeExp, median pop, and median gdpPercap
gdf_dict = df.groupby("year").agg(
    {
        "lifeExp": "mean",
        "pop": "median",
        "gdpPercap": "median"
    }
)

print(gdf_dict)

# %% 11-2
# Transform
# .transform() takes multiple values and returns a one-to-one transformation of the values
# that is, it does not reduce the amount of data
# Z-Score Example
def my_zscore(x):
    return (x-x.mean()) / x.std()


transform_z = df.groupby('year').lifeExp.transform(my_zscore)
print(transform_z.head())

# %%
# Missing Value Example
# randomly pick 4 'total_bill' values and turn them into missing
np.random.seed(42)
tips_10 = sns.load_dataset('tips').sample(10)
tips_10.loc[
    np.random.permutation(tips_10.index)[:4], 
    'total_bill'
] = np.NaN

print(tips_10)

# %%
# perhaps the Male and Female values in the sex column have different spending habits
# count the non-missing values by sex
count_sex = tips_10.groupby('sex').count()
print(count_sex)

# %%
def fill_na_mean(x):
    """returns the average of a given vector"""
    avg = x.mean()
    return x.fillna(avg)

# calculate a mean 'total_bill' by 'sex'
total_bill_group_mean = (
    tips_10
    .groupby("sex")
    .total_bill
    .transform(fill_na_mean)
)

# assign to a new column in the original data
# you can also replace the original column by using 'total_bill'
tips_10["fill_total_bill"] = total_bill_group_mean

print(tips_10[['sex', 'total_bill', 'fill_total_bill']])

# %% 11-3
# Filter
# .filter() allows you to split your data by keys,
# and then perform some kind of boolean subsetting on the data.

# load the tips data set
tips = sns.load_dataset('tips')

# note the number of rows in the original data
print(tips.shape)

# look at the frequency counts for the table size
print(tips['size'].value_counts())

# %%
# filter the data such that each group has more than 30 observations
tips_filtered = (
    tips
    .groupby("size")
    .filter(lambda x: x["size"].count() >= 30)
)

# the output shows that our data set was filtered down
print(tips_filtered.shape)
print(tips_filtered['size'].value_counts())

# %% 11-4
# The Object: pandas.core.groupby, DataFrameGroupby
# we will investigate some of the inner workings of grouped objects.

# start with the subsetted tips data set
tips_10 = sns.load_dataset('tips').sample(10, random_state=42)
print(tips_10)

# %%
# save just the grouped object
grouped = tips_10.groupby('sex')
# note that we just get back the object and its memory location
print(grouped)

# %%
# nothing has been actually calculated yet,
# because we never performed an action that requires a calculation
# if we want to actually see the calculated groups, we can call the groups attribute

# see the actual grops of the groupby
# it returns only the index
print(grouped.groups)

# %%
# calculate the mean on relevant columns
avgs = grouped.mean(numeric_only=True)
print(avgs)

# not all the columns reported a mean
# list all the columns
print(tips_10.columns)

# %%
# Selecting a Group

# to extract a particular group, use the .get_group() method
# get the 'Female' group
female = grouped.get_group('Female')
print(female)

# %%
# iterate through our grouped values just like any other container in Python
for sex_group in grouped:
    print(sex_group)

# %%
# you can't really get the 0 element from the grouped object
# the object is still a pandas.core.groupby.DataFrameGroupBy object
print(grouped[0])

# %%
# DataFrameGroupBy consists of tuple (key[string], group[DataFrame])
for key, group in grouped:
    print('* key:', key)
    print('* group:', len(group))
    print(group)
    print('\n')

# %%
# Multiple Groups
# mean by sex and time
bill_sex_time = tips_10.groupby(['sex', 'time'])
group_avg = bill_sex_time.mean(numeric_only=True)
print(group_avg)

# %%
# interesting things happen when we look at the index
print(group_avg.index)

# %%
# to get a regualr flat dataframe back,
# call the .reset_index() method on the results
group_method = (
    tips_10
    .groupby(['sex', 'time'])
    .mean(numeric_only=True)
    .reset_index()
)
print(group_method)

# %%
# alternatively, use the as_index=False parameter in the .groupby() method
group_param = (
    tips_10
    .groupby(['sex', 'time'], as_index=False)
    .mean(numeric_only=True)
)
print(group_param)
