students = [
    "Student1", "Student2", "Student3", "Student4", "Student5",
    "Student6", "Student7", "Student8", "Student9", "Student10",
    "Student11", "Student12", "Student13", "Student14", "Student15",
    "Student16", "Student17", "Student18", "Student19", "Student20"
]


# appending the data means adding the data at the last
# appending the data at the end of the list

# print(students)
students.append('temprory student 1')
# print(students)

# adding the multipple objects in the list is unspooerted by the python

# -----------------------> Note <----------------------------------------#

#students.append('temp1','temp2','temp3')
#    students.append('temp1','temp2','temp3')
#    TypeError: list.append() takes exactly one argument (3 given)

# -------------------------------------------------------------------------------

# adding the list to the existing list

students.append(['atharv ','parag','babu'])
# print(students)
# output ----->
# ['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6', 'Student7',
# 'Student8', 'Student9', 'Student10', 'Student11', 'Student12', 'Student13', 'Student14',
# 'Student15', 'Student16', 'Student17', 'Student18', 'Student19', 'Student20',
# 'temprory student 1', ['atharv ', 'parag', 'babu']]
