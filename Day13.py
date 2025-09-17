import pandas as pd
import numpy as np
data = {
    "Name": ["Asha", "Rahul", "Meena", "Kavi", "Rahul", None],
    "Age": [20, 22, np.nan, 21, 22, 23],
    "Score": [85, None, 76, 88, 92, 85]
}
df = pd.DataFrame(data)
print("Original dataframe: ")
print(df)

#drop duplicates
print("After removal of duplicates: ")
df = df.drop_duplicates()
print(df)

#To check whether any null value is present
print("Checks whether there's any null value present: ")
print(df.isnull())

#Count of missing value
print("Count of missing values: ")
print(df.isnull().sum())

#To fill missing values
df["Age"].fillna(df["Age"].mean(), inplace = True)
df["Score"].fillna(0,inplace=True)

#To drop rows with missing value
df = df.dropna()
print(df)

#To rename columns
df.rename(columns={"Name" : "Name_of_students", "Score":"Marks"}, inplace=True)
print(df) 