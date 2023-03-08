# %%
###############
## CHAPTER 5 ##
###############
import pandas as pd

# %% 05-2 
# concatenate data - row
df1 = pd.read_csv('./data/concat_1.csv')
df2 = pd.read_csv('./data/concat_2.csv')
df3 = pd.read_csv('./data/concat_3.csv')

row_concat = pd.concat([df1, df2, df3])
print(row_concat)

# %%
# add series to dataframe
new_row_series = pd.Series(['n1', 'n2', 'n3', 'n4'])
print(pd.concat([df1, new_row_series]))

# %%
# add dataframe to another dataframe
new_row_df = pd.DataFrame([['n1', 'n2', 'n3', 'n4']], 
                          columns=['A', 'B', 'C', 'D'])
print(pd.concat([df1, new_row_df]))

# %% 
# append method - deprecated
data_dict = {'A': 'n1', 
             'B': 'n2',
             'C': 'n3',
             'D': 'n4'}
print(df1.append(data_dict, ignore_index=True))

# %%
# instead of using append method
print(pd.concat(
    [df1, pd.DataFrame([data_dict.values()], columns=df1.columns)], 
    ignore_index=True)
    )

# %%
# reset row index
row_concat_i = pd.concat([df1, df2, df3], ignore_index=True)
print(row_concat_i)

# %%
# concatenate data - column
col_concat = pd.concat([df1, df2, df3], axis=1)
print(col_concat)

# %%
# extract columns by same column name
print(col_concat['A'])

# %%
# add a new column
col_concat['new_col_list'] = ['n1', 'n2', 'n3', 'n4']
print(col_concat)

# %%
# reset column index
print(pd.concat([df1, df2, df3], axis=1, ignore_index=True))

# %%
# inner join: concatenate dataframe with same index
df1.columns = ['A', 'B', 'C', 'D']
df2.columns = ['E', 'F', 'G', 'H']
df3.columns = ['A', 'C', 'F', 'H']

row_concat = pd.concat([df1, df2, df3])
print(row_concat)       # show many NaN data
print(pd.concat([df1, df3], ignore_index=False, join='inner'))

df1.index = [0, 1, 2, 3]
df2.index = [4, 5, 6, 7]
df3.index = [0, 2, 5, 7]

col_concat = pd.concat([df1, df2, df3], axis=1)
print(col_concat)       # show many NaN data
print(pd.concat([df1, df3], axis=1, join='inner'))

# %% 05-3
person = pd.read_csv('./data/survey_person.csv')
site = pd.read_csv('./data/survey_site.csv')
survey = pd.read_csv('./data/survey_survey.csv')
visited = pd.read_csv('./data/survey_visited.csv')

print(person)
print(site)
print(survey)
print(visited)

# %% an example of merge dataframe
visited_subset = visited.loc[[0, 2, 6], ]

o2o_merge = site.merge(visited_subset, left_on='name', right_on='site')
print(o2o_merge)

m2o_merge = site.merge(visited, left_on='name', right_on='site')
print(m2o_merge)

# %% other examples of merge dataframe
ps = person.merge(survey, left_on='ident', right_on='person')
vs = visited.merge(survey, left_on='ident', right_on='taken')
print(ps)
print(vs)

# %% many input values on 'left_on'
ps_vs = ps.merge(vs, 
                 left_on=['ident', 'taken', 'quant', 'reading'],
                 right_on=['person', 'ident', 'quant', 'reading']
                 )
print(ps_vs.loc[0,])
