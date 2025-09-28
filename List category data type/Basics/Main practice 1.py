students=[]

name = input("Enter your Name : ")

for n in name:
    students.append(n)
print(students)

name_of_student=(list)(students)

print(len(students)==len(name))
print(type(students),type(name))
print("Typecasting from list to list ",name_of_student)