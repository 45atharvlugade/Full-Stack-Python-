students=['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6', 'Student7', 'Student8', 'Student9', 'Student10', 'Student11', 'Student12', 'Student13', 'Student14', 'Student15', 'Student16', 'Student17', 'Student18', 'Student19', 'Student20']

# initial content of the objects is same

# memory address address of both the objects is same

# modification are independent

students_=students

print(id(students) , id(students_) , id(students_)==id(students))

# output ---- >

# 2323011912064 2323011912064 True

students_.append('Chatur Lugade')

print(students)
print(students_)

# Output
#['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6', 'Student7', 'Student8', 'Student9', 'Student10', 'Student11', 'Student12', 'Student13', 'Student14', 'Student15', 'Student16', 'Student17', 'Student18', 'Student19', 'Student20', 'Chatur Lugade']
#['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6', 'Student7', 'Student8', 'Student9', 'Student10', 'Student11', 'Student12', 'Student13', 'Student14', 'Student15', 'Student16', 'Student17', 'Student18', 'Student19', 'Student20', 'Chatur Lugade']

