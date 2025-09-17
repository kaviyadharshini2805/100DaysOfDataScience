import pandas as pd

students = pd.DataFrame({
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Asha", "Rahul", "Meena", "Kavi", "Ravi"],
    "Dept": ["CSE", "IT", "ECE", "CSE", "IT"]
})

marks = pd.DataFrame({
    "ID": [1, 2, 3, 5, 6],
    "Marks": [85, 90, 76, 92, 88]
})

# Inner Join
merged1 = pd.merge(students, marks, on="ID", how="inner")
print("Inner join:\n", merged1)

# Outer Join
merged2 = pd.merge(students, marks, on="ID", how="outer")
print("\nOuter join:\n", merged2)

# Concatenating two departments (IT + CSE only)
it_students = students[students["Dept"] == "IT"]
cse_students = students[students["Dept"] == "CSE"]

df_concat = pd.concat([it_students, cse_students], axis=0, ignore_index=True)
print("\nConcatenation of IT & CSE departments:\n", df_concat)