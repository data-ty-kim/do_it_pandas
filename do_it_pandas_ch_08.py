# %%
##########################
######## CHAPTER 8 #######
##########################
####### Data Types #######
##########################

# %% import modules
import pandas as pd
import seaborn as sns

# %% 08-1
# Data Types
tips = sns.load_dataset("tips")
tips.head()
tips.dtypes

# %% to convert into strings, use the astype() method
tips['sex_str'] = tips['sex'].astype(str)
print(tips.dtypes)

# %%
# to convert variables into numeric values, use to_numeric()
tips_sub_miss = tips.head(10)
tips_sub_miss.loc[[1, 3, 5, 7], 'total_bill'] = 'missing'
print(tips_sub_miss)

# %% total_bill column is a string object 
print(tips_sub_miss.dtypes) # 'total_bill' is object

# %% 'ignore', then invalid parsing will return the input
tips_sub_miss['total_bill'] = pd.to_numeric(
                                tips_sub_miss['total_bill'],
                                errors='ignore'
                                )
print(tips_sub_miss.dtypes)    # still object

# %% 'coerce', then invalid parsing will be set as NaN
tips_sub_miss['total_bill'] = pd.to_numeric(
                                tips_sub_miss['total_bill'],
                                errors='coerce'
                                )
print(tips_sub_miss.dtypes)    # get NaN values for the string

# %% downcast
tips_sub_miss['total_bill'] = pd.to_numeric(
                                tips_sub_miss['total_bill'],
                                errors='coerce',
                                downcast='float'
                                )
print(tips_sub_miss.dtypes)    # turns into float32

# %% 08-2
# Categorical Data
## - It can be memory and speed efficient to store data in this manner, 
## expecially if the data set includes many repeated string values
## - Categorical data may be appropriate when a column of values has an order (e.g., a Likert scale)
## - Some python libraries understand how to deal with categorical data (e.g., when fitting statistical models)

# %%
# Convert to Category
# conver the sex column into a string object first
tips['sex'] = tips['sex'].astype('str')
print(tips.info())      # memory usage: 10.8+ KB

# %%
# convert the sex column back into categorical data
tips['sex'] = tips['sex'].astype('category')
print(tips.info())      # memory usage: 9.3+ KB
