import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Names":["A","B","C","D","E"],
    "Maths":[85, 90, 78, 92, 88],
    "Science":[80, 85, 75, 90, 87],
    "English":[82, 88, 80, 85, 90]
}

df = pd.DataFrame(data)

print("First five rows:\n",df.head())
print("\nDataFrame Info:")
print(df.info())
print("Summary Statistics:\n",df.describe())

#Data Analysis
avg_scores = df[["Maths","Science","English"]].mean()
print("\nAverage Scores:\n", avg_scores)

topper = df.loc[df[["Maths","Science","English"]].mean(axis=1).idxmax()]
print("\nTopper Details:\n", topper)


#Visualizations

#Bar Chart
avg_scores.plot(kind='bar', color=['blue', 'orange', 'green'])
plt.title("Average Scores in Subjects")
plt.xlabel("Subjects")
plt.ylabel("Average Scores")
plt.show()
plt.savefig("barchart.png",dpi=150)

#Pie Chart
plt.figure()
plt.pie(avg_scores, labels=avg_scores.index, autopct='%1.1f%%', startangle=90)
plt.title("Average Scores Distribution")
plt.show()
plt.savefig("piechart.png",dpi=150)

#Line chart
df.plot(x="Names", y=["Maths","Science","English"], marker='o')
plt.title("Scores of Students in Different Subjects")
plt.xlabel("Students")
plt.ylabel("Scores")
plt.legend(title="Subjects")
plt.show()
plt.savefig("linechart.png",dpi=150)

#Box Plot
df[["Maths","Science","English"]].plot(kind='box')
plt.title("Score Distribution in Subjects")
plt.ylabel("Scores")
plt.show()
plt.savefig("boxplot.png",dpi=150)