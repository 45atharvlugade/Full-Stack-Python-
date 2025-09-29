# Q6) Remove the third element from a list.

import random

students_=[]

for _ in range(10) :
    number=random.randint(1,100000)
    temp=(f'Student{number}')
    if(temp not in students_) :
        students_.append(temp)
print(students_)
# output ----> ['Student69685', 'Student60752', 'Student94251', 'Student58869', 'Student14797', 'Student47475', 'Student6763', 'Student72048', 'Student9771', 'Student65251']
students_.remove(students_[3])
print(students_)
# output ----> ['Student69685', 'Student60752', 'Student94251', 'Student14797', 'Student47475', 'Student6763', 'Student72048', 'Student9771', 'Student65251']
