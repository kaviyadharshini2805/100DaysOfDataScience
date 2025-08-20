def mark_analysis(marks):
    avg_mark = sum(marks)/len(marks) #Calculates average
    highest_mark = max(marks) #Calculates highest
    lowest_mark = min(marks) #Calculates lowest

    print(f"Average mar: {avg_mark:.2f}")
    print(f"Highest mark: {highest_mark}")
    print(f"Lowest mark: {lowest_mark}")

#Getting input from user
n = int(input("Enter number of students: "))
marks = []
for i in range(n):
    mark = int(input(f"Enter mark of student{i+1}: "))
    marks.append(mark)

mark_analysis(marks)