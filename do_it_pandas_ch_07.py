# %%
##########################
######## CHAPTER 7 #######
##########################
# Tidy Data by Reshaping #
##########################

# %% import modules
import pandas as pd
import os
import urllib.request

# %% 07-1
# income and religion in the US from the Pew Research Center
pew = pd.read_csv('./data/pew.csv')
print(pew.iloc[:, 0:6])

# %% 
# melt method
pew_long = pd.melt(pew, id_vars='religion')
print(pew_long)

# %% 
# the melted/unpivoted columns are named
pew_long = pd.melt(pew, id_vars='religion', 
                   var_name='income', value_name='count')
print(pew_long)

# %%
# the Billboard dataset
billboard = pd.read_csv('./data/billboard.csv')
print(billboard.iloc[0:5, 0:16])

# %%
# melt the billboard data
billboard_long = pd.melt(
    billboard, 
    id_vars=['year', 'artist', 'track', 'time', 'date.entered'],
    var_name='week',
    value_name='rating'    
    )
print(billboard_long.head())

# %% 07-2
# Columns contain multiple variables
ebola = pd.read_csv('./data/country_timeseries.csv')
print(ebola.iloc[:5, [0,1,2,3,10,11]])

# %%
# melt the ebola data
ebola_long = pd.melt(ebola, id_vars=['Date', 'Day'])
print(ebola_long.head())

# %%
# get the variable column
# access the string methods
# and split the column by a delimiter
variable_split = ebola_long.variable.str.split('_')
print(variable_split)
print(type(variable_split))     # series
print(type(variable_split[0]))  # list


# %%
# to assign them to a new column
status_values = variable_split.str.get(0)
country_values = variable_split.str.get(1)

print(status_values[:5])
print(status_values[-5:])
print(country_values[:5])
print(country_values[-5:])

# %%
# add them to our dataframe
ebola_long['status'] = status_values
ebola_long['country'] = country_values
print(ebola_long.head())

# %% 07-3
# Variables in both rows and columns
weather = pd.read_csv('./data/weather.csv')
print(weather.iloc[:5, :])

# %%
# melt/unpivot the day values
weather_melt = pd.melt(
                weather, 
                id_vars=['id', 'year', 'month', 'element'],
                var_name='day',
                value_name='temp'
                )
print(weather_melt.head())

# %%
# to pivot up the variables
weather_tidy = weather_melt.pivot_table(
                index=['id', 'year', 'month', 'day'],
                columns='element',
                values='temp'
                )
print(weather_tidy)

# %%
# reset the index
weather_tidy_flat = weather_tidy.reset_index()
print(weather_tidy_flat.head())

# %% 07-4
# Multiple Observational Units in a table
print(billboard_long.shape)     # (24092, 7)
print(billboard_long.head())

# %%
# this table actually holds 2 types of data: 
# the track information and weekly ranking
print(billboard_long[billboard_long.track == 'Loser'].head())

# %%
# year, artist, track, time, and date.entered in a new dataframe 
# and each unique set of values be assigned a unique ID. 
# We can then use this unique ID in a second dataframe that
# represents a song, date, week number, and ranking.
billboard_songs = billboard_long[
                    ['year', 'artist', 'track', 'time']
                    ]
print(billboard_songs.shape)    # (24092, 4)

# %%
# to drop the duplicate rows
billboard_songs = billboard_songs.drop_duplicates()
print(billboard_songs.shape)    # (317, 4)

# %%
# to assign a unique value to each row of data
billboard_songs['id'] = range(len(billboard_songs))
print(billboard_songs.head(n=10))

# %%
# Merge the song dataframe to the original dataset
billboard_ratings = billboard_long.merge(
                        billboard_songs, 
                        on=['year', 'artist', 'track', 'time']
                        )
print(billboard_ratings.shape)
print(billboard_ratings.head())

# %%
# Finally, we subset the columns 
# to the ones we want in our ratings dataframe
print(billboard_ratings[['id', 'date.entered', 'week', 'rating']].head())
