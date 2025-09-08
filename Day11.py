import pandas as pd

df = pd.read_csv("K:\\100 Days of Data Science\\DAY-9\\Students_Performance.csv")

print("First 5 rows:\n", df.head(), "\n")

print("Average Marks by Department:\n", df.groupby("Department")["Marks"].mean(), "\n")
print("Count of Students by Department:\n", df.groupby("Department")["Name"].count(), "\n")

print("Summary (min, max, mean) by Department:\n",
df.groupby("Department")["Marks"].agg(["min", "max", "mean"]), "\n")

print("Number of Students in each Department:\n", df["Department"].value_counts(), "\n")

print("Students with Marks > 85:\n", df[df["Marks"] > 85], "\n")

print("Students in CSE or ECE Department:\n",
df[(df["Department"] == "CSE") | (df["Department"] == "ECE")], "\n")

df2 = df.set_index("Name")
print("Accessing by Name index (E):\n", df2.loc["E"], "\n")

df.groupby("Department")["Marks"].mean().to_csv("Dept_Avg_Marks.csv")
print("Exported average marks by department to Dept_Avg_Marks.csv")
