# Q4) Append the number 99 to a list and print the updated list.

students_=[]
import random
for _ in range(10) :
    number=random.randint(1,1999)
    temp_student_=(f'Student{number}')
    if(temp_student_ not in students_) :
        students_.append(temp_student_)

print(students_)

students_.append('Student111111')
print(students_)

#Output ---------------------------------->
#['Student1715', 'Student501', 'Student1035', 'Student1770', 'Student1010', 'Student41', 'Student1263', 'Student628', 'Student988', 'Student1999']

#['Student1715', 'Student501', 'Student1035', 'Student1770', 'Student1010', 'Student41', 'Student1263', 'Student628', 'Student988', 'Student1999', 'Student111111']
