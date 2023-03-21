# %%
##########################
####### CHAPTER 12 #######
##########################
##### Dates and Times ####
##########################

# %%
# import modules
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# %% 12-1
# Python's datetime Object

# use datetime to get the current date and time
now = datetime.now()
print(f'Last time this chapter was rendered for print: {now}')

# %%
# create own datetime manually
t1 = datetime.now()
t2 = datetime(1970, 1, 1)
t3 = datetime(1970, 12, 12, 13, 24, 34)
print(t1)
print(t2)
print(t3)

# %%
# do datetime math
diff1 = t1 - t2
print(diff1)
print(type(diff1))

# %%
diff2 = t2 - t1
print(diff2)
print(type(diff2))

# %%
# convert the Date column into a proper datetime object
ebola = pd.read_csv('./data/country_timeseries.csv')

# top left corner of the data
print(ebola.iloc[:5, :5])

# Date column is encoded as a generic string object in Pandas
print(ebola.info())

# %%
# create a new column, date_dt,
# that converts the Date column into a datetime
ebola['date_dt'] = pd.to_datetime(ebola['Date'])
print(ebola.info())

# %%
# The to_datetime() function has a parameter called format
# that allows you to manually specify the format of the date
# you are hoping to parse.
test_df1 = pd.DataFrame(
    {'order_day': ['01/01/15', '02/01/15', '03/01/15']}
    )

test_df1['date_dt1'] = pd.to_datetime(test_df1['order_day'], format='%d/%m/%y')
test_df1['date_dt2'] = pd.to_datetime(test_df1['order_day'], format='%m/%d/%y')
test_df1['date_dt3'] = pd.to_datetime(test_df1['order_day'], format='%y/%m/%d')
print(test_df1)

test_df2 = pd.DataFrame(
    {'order_day':['01-01-15', '02-01-15', '03-01-15']}
    )

test_df2['date_dt'] = pd.to_datetime(test_df2['order_day'], format='%d-%m-%y')
print(test_df2)

# %%
# Using strftime() method to extract time
now = datetime.now()
print(now)

nowDate = now.strftime('%Y-%m-%d')
print(nowDate)

nowTime = now.strftime('%H:%M:%S')
print(nowTime)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)

# %%
# Loading Data That Include Dates
# parse the Date column directly 
# by specifying the column we want in the parse_dates parameter

ebola1 = pd.read_csv('./data/country_timeseries.csv', parse_dates=['Date'])
print(ebola1.info())

# %%
# Extracting Date Components
# extract various parts of the date, such as year, month, or day
d = pd.to_datetime('2021-12-14')
print(d)

print(d.year)
print(d.month)
print(d.day)

# %%
# using the .dt. accessor
ebola['date_dt'] = pd.to_datetime(ebola['Date'])
print(ebola[['Date', 'date_dt']])

ebola['year'] = ebola['date_dt'].dt.year
print(ebola[['Date', 'date_dt', 'year']])

ebola = ebola.assign(
    month=ebola['date_dt'].dt.month,
    day=ebola['date_dt'].dt.day
)
print(ebola[['Date', 'date_dt', 'year', 'month', 'day']].head())

# %%
# when we parsed out our dates, the data type was not preserved.
print(ebola.info())     # year, month, day are int64

# %% 12-2
# Date Calculations and Timedeltas
# One of the benefits of having data objects is being able to do date calculations

# to see the first day of the outbreak
print(ebola.iloc[-5:, :5])

# %%
# using the .min() method of the column
print(ebola['date_dt'].min())

# %%
# calculation
ebola['outbreak_d'] = ebola['date_dt'] - ebola['date_dt'].min()
print(ebola[['Date', 'Day', 'outbreak_d']])

# %%
# end up with a timedelta object
print(ebola.info())

# %%
# Datetime Methods
# another data set: bank failures
banks = pd.read_csv('./data/banklist.csv')
print(banks.head())

# %%
# import data with the dates directly parsed
banks = pd.read_csv(
    "./data/banklist.csv", parse_dates=[5, 6]
)
print(banks.info()) 

# %%
# parse out the date by obtaining the quarter and year in which the bank closed
banks = banks.assign(
    closing_quarter=banks['Closing Date'].dt.quarter,
    closing_year=banks['Closing Date'].dt.year
)
closing_year = banks.groupby(['closing_year']).size()
print(closing_year)

# %%
# how many banks closed in each quarter of each year
closing_year_q = (
    banks
    .groupby(['closing_year', 'closing_quarter'])
    .size()
)
print(closing_year_q)

# %%
# plot the results
fig, ax = plt.subplots()
ax = closing_year.plot()
plt.show()

fig, ax = plt.subplots()
ax = closing_year_q.plot()
plt.show()

# %%
# show plots in one frame
fig, ax = plt.subplots(1,2, figsize=(12,5))
closing_year.plot(ax=ax[0])
closing_year_q.plot(ax=ax[1])
plt.show()

# %%
# Getting Stock Data
# get stock information about Tesla
tesla = pd.read_csv('./data/tesla_stock_quandl.csv')
print(tesla.head())

# %%
# Subsetting Data Based on Dates
tesla = pd.read_csv(
    './data/tesla_stock_quandl.csv', 
    parse_dates=[0]
    )

print(
    tesla.loc[
        (tesla.Date.dt.year == 2010) & (tesla.Date.dt.month ==6)
    ]
)

# %%
# The DatetimeIndex Object

# assign the Date column as the index
tesla.index = tesla['Date']
print(tesla.index)

# %%
# with the index set as a date object, we can use the date directly to subset rows
print(tesla.loc['2015'].iloc[:5, :5])

# %%
# subset the data based on the year and month
print(tesla.loc['2010-06'].iloc[:,:5])

# %%
# The TimedeltaIndex Object

# set the index of a dataframe to a timedelta 
# to create TimedeltaIndex
tesla['ref_date'] = tesla['Date'] - tesla['Date'].min()
tesla.index = tesla['ref_date']
print(tesla.head())

# %%
print(tesla.loc['5 days':].iloc[:,:5])
print(tesla.loc['10 day': '0 day'])

# %%
# Date Ranges
# in Ebola data set, there is a missing day in the date range.

# 2015-01-01 is missing from the data
ebola = pd.read_csv('./data/country_timeseries.csv', parse_dates=[0])
print(ebola.iloc[:, :5])

# %%
# use the date_range()
head_range = pd.date_range(start='2014-12-31', end='2015-01-05')
print(head_range)

# %%
# work with the first five rows in the example
ebola_5 = ebola.head()
ebola_5.index = ebola_5['Date']
ebola_5 = ebola_5.reindex(head_range)
print(ebola_5.iloc[:, :5])

# %%
# Shifting Values

# standardize the start dates for data to compare trends
# Ebola plot has unshifted dates
ebola.index = ebola['Date']
fig, ax =plt.subplots()
ebola.iloc[0:, 1:].plot(ax=ax)
ax.legend(fontsize=7, loc=2, borderaxespad=0.) 
    # loc=2 means 'upper left'
    # borderaxespad: The pad between the axes and legend border
plt.show()

# %%
# look at just a few columns from Ebola data set
ebola_sub = ebola[['Day', 'Cases_Guinea', 'Cases_Liberia']]
print(ebola_sub.tail(10))

# %%
# load Ebola data set 
# parsing the Date column as a proper date object and assigning this date to the .index
ebola = pd.read_csv(
    './data/country_timeseries.csv', 
    index_col='Date',
    parse_dates=['Date']
    )
print(ebola.iloc[:, :4])

# %%
# create the date range to fill in all the missing dates
new_idx = pd.date_range(ebola.index.min(), ebola.index.max())
new_idx = pd.DatetimeIndex(reversed(new_idx))
# or do this way: new_idx = new_idx[::-1]
# print(new_idx)

# %%
# .reindex() the data, and this will create rows of NaN values
ebola = ebola.reindex(new_idx)
print(ebola.iloc[:,:4])

# %%
# .last_valid_index() method
# which returns the label(index) of the last non-missing or non-null value
last_valid = ebola.apply(pd.Series.last_valid_index)
print(last_valid)

# %%
# get the earliest date in data set
earliest_date = ebola.index.min()
print(earliest_date)

# %%
# to calculate the difference between the earliest date and earliest valid date
shift_values = last_valid - earliest_date
print(shift_values)

# %%
# ebola_dict = {}
# for idx, col in enumerate(ebola):
#     print(idx)
#     print(col)

print(ebola.head())




# %%
# we can iterate through each column,
# using the .shift() method to shift the columns down
# by the corresponding value in shift_values.
ebola_dict = {}
for idx, col in enumerate(ebola):
    d = shift_values[idx].days
    shifted = ebola[col].shift(d)
    ebola_dict[col] = shifted

# %%
# convert a dict to a dataframe
ebola_shift = pd.DataFrame(ebola_dict)
print(ebola_shift.tail())

# %%
# assign the correct index, the Day
ebola_shift.index = ebola_shift['Day']
ebola_shift = ebola_shift.drop(['Day'], axis=1)
print(ebola_shift.tail())
