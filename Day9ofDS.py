import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("K:\\100 Days of Data Science\\DAY-9\\Students_Performance.csv")

print("First 5 rows:\n",df.head())

print("\Data Info:\n")
df.info()

print("Summary Statistic: \n",df.describe())

#Highest Scores
print("High Marks:\n")
print(df[df["Marks"] > 85])

#Students in CSE
print("Students in CSE:\n",df[df["Department"] == "CSE"])

#Students with low attendance
print("Students with attendance(%) less than 75:\n",df[df["Attendance (%)"] < 75])

#Average Marks per Department
print("Average Marks per Department:\n",df.groupby("Department")["Marks"].mean())

#Average Attendance by Department
print("Average Attendance by Department: \n",df.groupby("Department")["Attendance (%)"].mean())

#Bar Chart to visualize Average Marks by Department
df.groupby("Department")["Marks"].mean().plot(kind="bar",title="Average Marks by Department")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.show()

#Scatter Plot to visualize Marks versus Attendance
plt.scatter(df["Marks"], df["Attendance (%)"])
plt.title("Marks vs Attendance")
plt.xlabel("Marks")
plt.ylabel("Attendance (%)")
plt.show()

#Histogram to visualize the distribution of Marks
plt.hist(df["Marks"], bins=10, edgecolor = "black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()