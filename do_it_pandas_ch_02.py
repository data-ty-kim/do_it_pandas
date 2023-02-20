import pandas as pd

df = pd.read_csv('./data/gapminder.tsv', sep='\t')

print(df.head())