students=['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6', 'Student7', 'Student8', 'Student9', 'Student10', 'Student11', 'Student12', 'Student13', 'Student14', 'Student15', 'Student16', 'Student17', 'Student18', 'Student19', 'Student20']


print(students)
del(students[12])

print(students,id(students))
del(students[11])
print(students,id(students))
del(students[9])

students.pop(12)
print('I m here -------------------->')
print(students,id(students))




