'''
Problem #2
you have a list of student names and another list with their marks in CS. 
hard code the values. no need to get it as input
Pass mark is 50.
Print a new list with all the students with pass marks along with their mark in the format name:mark.
Also print the number of students who failed.
'''
#get the student name list and mark list
students_name_list=['ram','raja','rani','ramesh','raji']
cs_mark_list=[45,97,97,49,90]
#initialize the failed student count is 0
count_no_student_failed=0
#use for loop for iteration
for student_list in range (len(students_name_list)):
    #check the condition mark greater than 50 then print name:mark 
    if cs_mark_list[student_list] >= 50:
         print(f"{students_name_list[student_list]}:{cs_mark_list[student_list]}")
    #else count the failed students  
    else:
       count_no_student_failed+=1
#print the failed student count
print(f"failed students count: {count_no_student_failed}")

'''
output:

raja:97
rani:97
raji:90
failed students count: 2
'''