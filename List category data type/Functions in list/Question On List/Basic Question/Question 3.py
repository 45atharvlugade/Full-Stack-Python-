import random
# Q3 )How do you access the first and last elements of a list?
students_=[]

for _ in range(100) :
    number=random.randint(1,100)
    temp_=(f'Student{number}')
    if temp_ not in students_ :
       students_.append(temp_)
print(students_)
print(students_[0])
print(students_[len(students_)-1])

# output -------->
#['Student54', 'Student50', 'Student46', 'Student68', 'Student16', 'Student60', 'Student59', 'Student62', 'Student48', 'Student99', 'Student40', 'Student8', 'Student79', 'Student10', 'Student45', 'Student24', 'Student96', 'Student55', 'Student94', 'Student25', 'Student2', 'Student74', 'Student22', 'Student23', 'Student100', 'Student30', 'Student32', 'Student64', 'Student57', 'Student82', 'Student6', 'Student87', 'Student69', 'Student36', 'Student77', 'Student5', 'Student13', 'Student17', 'Student70', 'Student4', 'Student56', 'Student86', 'Student1', 'Student84', 'Student61', 'Student67', 'Student21', 'Student91', 'Student85', 'Student14', 'Student41', 'Student39', 'Student31', 'Student19', 'Student42', 'Student52', 'Student97', 'Student20', 'Student35', 'Student76', 'Student89', 'Student28', 'Student71', 'Student27', 'Student9', 'Student33']
#Student54
#Student33
