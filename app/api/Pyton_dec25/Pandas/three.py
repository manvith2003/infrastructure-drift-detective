import pandas as pd
import numpy as np

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [22, np.nan, 23, np.nan],
    "salary": [50000, 60000, np.nan, 45000]
}

df = pd.DataFrame(data)
print(df)

print(df.isna())
print(df.isna().sum())

df1=df.dropna()
print(df1)

df2=df.dropna(axis=1)
print(df2)

print(df.fillna(0))

df["age"]=df["age"].fillna(df["age"].mean())
df["salary"] =df["salary"].fillna(df["salary"].median())

print(df.fillna(method="bfill"))

print(df.fillna(method="ffill"))




