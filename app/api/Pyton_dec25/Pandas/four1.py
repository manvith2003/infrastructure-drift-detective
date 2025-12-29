import pandas as pd
import numpy as np


data = {
    "dept": ["IT", "IT", "HR", "HR"],
    "gender": ["M", "F", "M", "F"],
    "salary": [60000, 65000, 50000, 52000]
}

df = pd.DataFrame(data)
print(df)

df.head()
df.tail()
df.shape
df.columns
df.info()
df.describe()


print(df.groupby(["dept","gender"],as_index=False)["salary"].agg(["mean","max","median"]))

#custion functions


print(df.groupby("dept")["salary"].apply(lambda x :x.max()-x.min()))

