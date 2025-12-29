import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [22, 25, 23, 21],
    "salary": [50000, 60000, 55000, 48000]
}

df = pd.DataFrame(data)
print(df)


print(df.sort_values(by="salary",ascending=False))

print(df.sort_values(by=["age", "salary"]))

print(df.sort_index(ascending=False))

df_custom = df.set_index("name")
print(df_custom)

print(df_custom.sort_index(ascending=False))

print(df_custom.reset_index())



