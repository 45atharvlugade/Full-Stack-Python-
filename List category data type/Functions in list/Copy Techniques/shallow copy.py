students=['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6', 'Student7', 'Student8', 'Student9', 'Student10', 'Student11', 'Student12', 'Student13', 'Student14', 'Student15', 'Student16', 'Student17', 'Student18', 'Student19', 'Student20']

# the changes which are done on one object it will not affect others

# in shallow copy the memory  initial content is same but

# memory address are different

# for Example

students_=students.copy()
#print(students , id(students))
#print('0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
#print(students_,id(students_))

# output Inital Content , memeor Address

#['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6', 'Student7', 'Student8', 'Student9', 'Student10',
# 'Student11', 'Student12', 'Student13', 'Student14', 'Student15', 'Student16', 'Student17', 'Student18', 'Student19', 'Student20']
# Memory Address of students ---->1845740355968
#0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
#['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6', 'Student7', 'Student8', 'Student9', 'Student10',
# 'Student11', 'Student12', 'Student13', 'Student14', 'Student15', 'Student16', 'Student17', 'Student18', 'Student19', 'Student20']
# Memory Address of students_  ---->1845740311104


# __________________________________________________________________________________________________________________________________

# performing the operations on the both of the list individually

# -------------> Modifications can be dne individually [}{[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]j

#print('# performing the operations on the both of the list individually')
#tudents_.insert(9,'Parag Kadam')
#students.pop(9)

#print(students,"\n Memory Address :",id(students))
#print(students_,"\n  Memory Address :",id(students_))

# output

# ['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6', 'Student7', 'Student8', 'Student9', 'Student10',
# 'Student11', 'Student12', 'Student13', 'Student14', 'Student15', 'Student16', 'Student17', 'Student18', 'Student19', 'Student20']
# Memory Address  : ----- > 2293965242752
# 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# ['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6', 'Student7', 'Student8', 'Student9', 'Student10', 'Student11',
# 'Student12', 'Student13', 'Student14', 'Student15', 'Student16', 'Student17', 'Student18', 'Student19', 'Student20']
# Memeory Adddress : ------> 2293965197888
# # performing the operations on the both of the list individually
# ['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6', 'Student7', 'Student8', 'Student9', 'Parag Kadam', 'Student10', 'Student11', 'Student12', 'Student13', 'Student14', 'Student15', 'Student16', 'Student17', 'Student18', 'Student19', 'Student20']
#  Memory Address : 2293965197888
# ['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6', 'Student7', 'Student8', 'Student9', 'Student11', 'Student12', 'Student13', 'Student14', 'Student15', 'Student16', 'Student17', 'Student18', 'Student19', 'Student20']
#   Memory Address : 2293965242752
