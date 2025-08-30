
import matplotlib.pyplot as plt
import numpy as np

# Sample Data
np.random.seed(0)
study_hours = np.random.randint(1, 10, 20)
exam_scores = study_hours * 10 + np.random.randint(-10, 10, 20)

# 1. Scatter Plot
plt.scatter(study_hours, exam_scores, color='blue', marker='o')
plt.title("Study Hours vs Exam Scores")
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.grid(True)
plt.show()

# 2. Histogram
plt.hist(study_hours, bins=5, color='orange', edgecolor='black')
plt.title("Distribution of Study Hours")
plt.xlabel("Hours")
plt.ylabel("Frequency")
plt.show()

# 3. Boxplot
plt.boxplot(exam_scores)
plt.title("Exam Score Spread")
plt.ylabel("Scores")
plt.show()

# 4. Stacked Bar Chart
subjects = ["Math", "Science", "English"]
marks_boys = [80, 70, 90]
marks_girls = [85, 75, 95]

plt.bar(subjects, marks_boys, label="Boys")
plt.bar(subjects, marks_girls, bottom=marks_boys, label="Girls")
plt.title("Stacked Bar Chart of Marks")
plt.legend()
plt.show()
