'''
problem #5
In your college Python is taught in 3 different departments by the same professor. 
For each dept, get the no of students stutying Python and their marks in the final exam 
Get the input as comma seperated string
'''
#initialize or get the input for the no of departments
no_of_depts=3
#create a dictionary  for depatment wise mark list 
college_mark_list_deptwise={}
#iterate the for loop for get the no of students in each department
for dept in range (no_of_depts):
    no_of_students=int(input(f"enter the no of students studying python in department {dept+1}: "))
    #create a list for storing the mark list of each student
    marks_list=[]
    #iterate the for loop to get the marks from each students
    for student in range (no_of_students):
        marks=input(f"enter the no:{student+1} student marks  (comma seperated): ")
        #split the marks with comma
        marks=marks.split(',')
        #append the marks in mark list
        marks_list.append(marks)
    #add the depatment and student marks in the dictionary
    college_mark_list_deptwise[f"Department {dept + 1}"] = marks_list
#print the dict
print(college_mark_list_deptwise)





