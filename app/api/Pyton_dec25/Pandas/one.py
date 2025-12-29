import pandas as pd

s =pd.Series([10,20,30,40,50])

print(s)

i =pd.Series([10,20,30,40],index=["a","b","c","d"])

print(i)

print(i["b"])

data = {
    "Alice": 22,
    "Bob": 25,
    "Charlie": 23
}

a =pd.Series(data)
print(a)

print(a+1)

data1 = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [22, 25, 23],
    "salary": [50000, 60000, 55000]
}

df = pd.DataFrame(data1)
print(df)

print(df.shape)
print(df.columns)
print(df.index)

print(df["age"])