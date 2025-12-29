import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [22, 25, 23],
    "salary": [50000, 60000, 55000]
}

df = pd.DataFrame(data)
print(df)

print(df["salary"])

print(df[["name","salary"]])

#iloc

print(df.iloc[0])

print(df.iloc[1,2])

#exclusive iloc and inclusive loc

print(df.iloc[0:2,1:3])

print(df.loc[1])

print(df.loc[0:1,["name","salary"]])

#Boolean Filtering

print(df[df["age"]>23])

print(df[(df["age"] > 22) & (df["salary"] > 52000)])

#Modify Values (IMPORTANT)

df.loc[df["age"]<23 ,"salary"]=46787
print(df)




