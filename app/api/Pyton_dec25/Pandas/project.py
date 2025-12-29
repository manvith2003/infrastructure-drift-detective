import pandas as pd
import numpy as np

data = {
    "emp_id": [101, 102, 103, 104, 105],
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "dept": ["IT", "HR", "IT", "Finance", "HR"],
    "age": [22, 29, np.nan, 35, 26],
    "salary": [50000, 60000, 55000, np.nan, 58000]
}

df = pd.DataFrame(data)
print(df)

df.head()
df.shape
df.columns
df.info()


df["age"] =df["age"].fillna(df["age"].mean())
df["salary"] = df["salary"].fillna(df["salary"].median())

df["age_group"] = df["age"].apply(
    lambda x: "Young" if x < 25 else "Adult"
)

df["salary_level"] = df["salary"].apply(
    lambda x: "High" if x >= 58000 else "Low"
)

df.sort_values(by="salary", ascending=False)

a=df.groupby("dept")["salary"].mean()
count =df.groupby("dept")["emp_id"].count()

final_df = df[["age", "salary", "dept", "age_group", "salary_level"]]
print(final_df)

print(df)


