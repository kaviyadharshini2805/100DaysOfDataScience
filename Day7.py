import matplotlib.pyplot as plt
study_hours = [2, 4, 6, 8, 10, 12]
exam_scores = [40, 55, 65, 75, 90, 95]

#Subplot
plt.subplot(2,2,1)
plt.plot(study_hours,exam_scores,'b-o')
plt.title("Study Hours vs Exam Scores")

#Scatter Plot
plt.subplot(2,2,2)
plt.scatter(study_hours,exam_scores,color = "red")
plt.title("Scatter Plot")

#Histogram
plt.subplot(2,2,3)
plt.hist(study_hours,bins=5,color="orange",edgecolor="black")
plt.title("Histogram of Study")

#Boxplot
plt.subplot(2,2,4)
plt.boxplot(study_hours,patch_artist=True,boxprops=dict(facecolor = "green"))
plt.title("Boxplot of Study")
plt.savefig("study_hours_vs_exam_score.png",dpi=150)
plt.tight_layout()
plt.show()