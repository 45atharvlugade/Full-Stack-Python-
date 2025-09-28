students=['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6', 'Student7', 'Student8', 'Student9', 'Student10', ' Bhagwan ', 'Student11', 'Student12', 'Student13', 'Student14', 'Student15', 'Student16', 'Student17', 'Student18', 'Student19', 'Student20']


students.pop(10)
print(students)

students.pop(0)
print(students)

students.pop(-1)
print(students)

# students.pop(100) ======> IndexError: pop index out of range
print(students)
# [].pop() =====> IndexError: pop from empty list

students.pop()
print(students)   # last element is popped from the List[]

