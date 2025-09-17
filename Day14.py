import pandas as pd
import numpy as np

data = {
    "Name": ["Asha", "Rahul", "Meena", "Kavi", "Rahul", "Ravi", "Meena", "None"],
    "Age": [20, 22, np.nan, 21, 22, 23, 21, 20],
    "Score": [85, np.nan, 76, 88, 92, 85, np.nan, 70],
    "Department": ["CSE", " cse ", "ECE", "ECE", "cse", None, "ECE", "CSE"]
}

df = pd.DataFrame(data)
print(df)

# Filling the missing Age
print("\nFilling missing values in Age:")
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df)

# Filling the Score
print("\nFilling missing scores:")
df["Score"] = df["Score"].fillna(df["Score"].median())
print(df)

# Filling the department with "Unknown"
print("\nFilling missing values in Department:")
df["Department"] = df["Department"].fillna("Unknown")
print(df)

# Drop row Name where the value is missing
df["Name"] = df["Name"].replace("None", np.nan)
df = df.dropna(subset=["Name"])

# Remove trailing and leading spaces
print("\nAfter Removal of trailing and leading spaces:")
for column in df.select_dtypes(include=['object']).columns:
    df[column] = df[column].str.strip()
print(df)

# Convert Cases
print("\nConverting to Upper Case:")
for column in df.select_dtypes(include=['object']).columns:
    df[column] = df[column].str.upper()
print(df)

# Removal of duplicates
print("\nAfter removal of duplicates:")
df = df.drop_duplicates(subset=["Name"])
print(df)

# Renaming the columns
print("\nRenaming columns:")
df = df.rename(columns={"Score": "Marks", "Name": "FullName"})
print(df)

# Changing data types
df["Marks"] = df["Marks"].astype(int)
df["Age"] = df["Age"].astype(int)

print("\nCleaned Data:")
print(df)