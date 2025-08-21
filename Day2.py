import math
import matplotlib.pyplot as plt
#To calculate Standard Deviation
def Standard_Deviation(marks):
    #Step-1
    Sum = sum(marks)
    Mean = Sum / len(marks)
    print("Mean:", Mean)

    #Step-2
    Deviation_of_each = [ i - Mean for i in marks]
    print(f"Deviation: {Deviation_of_each}")

    #Step-3
    Squared_Deviation = [ i*i for i in Deviation_of_each]
    print(f"Squared values of Deviation: {Squared_Deviation}")

    #Step-4
    Variance = sum(Squared_Deviation)/len(Squared_Deviation)
    print(f"Variance: {Variance}")

    #Step-5
    Standard_Deviation = math.sqrt(Variance)
    print(f"Standard Deviation : {Standard_Deviation}")

names = ["Kavi", "Arjun", "Priya", "Ravi","Bhava"]
marks = [45, 67, 88, 76,98]

#Bar chart
plt.bar(names,marks)
plt.xlabel("Names")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()

#Line plot
plt.plot(names,marks,marker='*')
plt.xlabel("Names")
plt.ylabel("Marks")
plt.title("Student Marks Trend")
plt.show()

#Pie chart
plt.pie(marks,labels=names,autopct="%1.1f%%")
plt.title("Marks")
plt.show()