import csv 
import pandas as pd 
df = pd.read_csv("main.csv")
print(df.shape)
del df["Unnamed: 0.1"]
del df["Unnamed: 0"]
del df["Unnamed: 6"]
print(df.shape)
df.to_csv("all_stars.csv")