import pandas as pd

data = {
    "dept": ["IT", "IT", "HR", "HR", "Finance", "Finance"],
    "employee": ["A", "B", "C", "D", "E", "F"],
    "salary": [60000, 65000, 50000, 52000, 70000, 72000]
}

df = pd.DataFrame(data)
print(df)


print(df.groupby("dept")["salary"].mean())

#dataframe output

print(df.groupby("dept",as_index=False)["salary"].mean())

print(df.groupby("dept",as_index=False)["salary"].agg(["max","mean","min","median","count"]))

