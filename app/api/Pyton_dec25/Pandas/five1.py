import pandas as pd

employees = pd.DataFrame({
    "emp_id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"]
})

salaries = pd.DataFrame({
    "emp_id": [1, 2, 4],
    "salary": [50000, 60000, 70000]
})

print(employees)
print(salaries)


print(pd.merge(employees,salaries,on="emp_id"))

print(pd.merge(employees,salaries,on="emp_id",how="left"))
print(pd.merge(employees,salaries,on="emp_id",how="right"))
print(pd.merge(employees,salaries,on="emp_id",how="outer"))


