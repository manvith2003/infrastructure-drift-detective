import pandas as pd
import numpy as np

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [22, 25, 17, 35],
    "salary": [50000, 60000, 40000, 80000],
    "gender": ["F", "M", "M", "M"]
}

df = pd.DataFrame(data)
print(df)

df["binary"]=df["gender"].map({"M":1,"F":0})
df["age_group"] = df["age"].apply(lambda x : "Child" if x<19 else "Adult")

#slow roe wise its lise for loop
df["salary_level"] =df.apply(lambda r :"High" if r["salary"] > 60000 else "Low",axis=1)

#faster than above column vise so

df["salary_usa"] =df["salary"].apply(lambda x :"High" if x>100000 else "Low")

#even faster since it is vectorised 

df["salry_india"] =np.where(df["salary"] >89098 ,"High" ,"Low")

print(df)