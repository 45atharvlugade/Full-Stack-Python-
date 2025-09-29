# Q7) ow do you find the length of a list?


import random

students_=[]

for _ in range(10) :
    number=random.randint(1,100000)
    temp=(f'Student{number}')
    if(temp not in students_) :
        students_.append(temp)
print(len(students_))
# output -----> 10

