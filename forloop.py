'''
write code for both for and while loop
'''
#Get marks from 5  students and calculate avg
no_of_students=int(input("enter the number of students: "))
#for loop
total = 0
for student in range(no_of_students):
    #get user input student marks
     mark=float(input(f"enter the student {student+1} mark: "))
     total += mark
avg_mark=total/no_of_students
print ("Avg is ",avg_mark)

'''
output:

enter the number of students: 5
enter the student 1 mark: 100
enter the student 2 mark: 98
enter the student 3 mark: 90
enter the student 4 mark: 87
enter the student 5 mark: 90
Avg is  93.0
'''