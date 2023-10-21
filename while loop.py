'''
write code for both for and while loop
'''
#using while loop
total = 0
#Get marks from 5  students and calculate avg
no_of_students=int(input("enter the number of students: "))
student_count = 0
while (student_count < no_of_students):
   #get user input as student mark
     mark=float(input(f"enter the student {student_count+1} mark: "))
     total += mark
     student_count += 1
avg_mark=total/no_of_students
print ("Avg is ",avg_mark)

'''
enter the number of students: 5
enter the student 1 mark: 98
enter the student 2 mark: 69
enter the student 3 mark: 80
enter the student 4 mark: 70
enter the student 5 mark: 50
Avg is  73.4
'''