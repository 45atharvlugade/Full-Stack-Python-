

students = [
    "Student1", "Student2", "Student3", "Student4", "Student5",
    "Student6", "Student7", "Student8", "Student9", "Student10",
    "Student11", "Student12", "Student13", "Student14", "Student15",
    "Student16", "Student17", "Student18", "Student19", "Student20"
]
students.insert(10,'Atharv Raghunath Lugade ')
#
#print(students)
# out put ----->
# ['Student1', 'Student2', 'Student3', 'Student4', 'Student5',
# 'Student6', 'Student7', 'Student8', 'Student9', 'Student10',
# 'Atharv Raghunath Lugade ', 'Student11', 'Student12', 'Student13',
# 'Student14', 'Student15', 'Student16', 'Student17', 'Student18',
# 'Student19', 'Student20']

students.insert(-10,' Bhagwan ')
print(students)
# output ----->

# ['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6',
# 'Student7', 'Student8', 'Student9', 'Student10', 'Atharv Raghunath Lugade ',
# ' Bhagwan ', 'Student11', 'Student12', 'Student13', 'Student14', 'Student15',
# 'Student16', 'Student17', 'Student18', 'Student19', 'Student20']