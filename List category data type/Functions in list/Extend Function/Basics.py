# extedning the list

students=[]

for i in range (50) :
    temp_=f"Student{i}"
    students.append(temp_)

#print(students)

students_=[]
for i in range (50,100) :
    temp_=f"Students{i}"
    students_.append(temp_)

students.extend(students_)

print("Students    :",students)
print("Students_   :",students_)
