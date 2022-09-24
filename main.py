import pandas as pd

df1 = pd.read_csv("shared_articles.csv")
print(df1.head())

df2 = pd.read_csv("users_interactions.csv")
print(df2.head())