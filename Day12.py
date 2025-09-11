import matplotlib.pyplot as plt

students = ["A","B","C","D","E","F","G","H","I","J"]
math_marks = [45, 78, 88, 56, 95, 67, 72, 80, 60, 50]
science_marks = [52, 74, 90, 60, 99, 72, 69, 85, 65, 58]

plt.figure(figsize=(6,4))
plt.scatter(math_marks, science_marks, color='blue', marker='o')
for i, name in enumerate(students):
    plt.text(math_marks[i]+0.5, science_marks[i]+0.5, name)  

plt.title("Student Performance: Math vs Science")
plt.xlabel("Math Marks")
plt.ylabel("Science Marks")
plt.grid(True)
plt.show()

ages = [15, 18, 19, 21, 22, 22, 23, 24, 25, 27, 28, 
        30, 31, 31, 32, 35, 36, 38, 40, 42, 43, 
        45, 47, 50, 52, 55, 60, 65, 70, 72]

plt.figure(figsize=(6,4))
plt.hist(ages, bins=8, color='green', edgecolor='black')
plt.title("Histogram: Age Distribution of Students")
plt.xlabel("Age Groups")
plt.ylabel("Frequency")
plt.show()
