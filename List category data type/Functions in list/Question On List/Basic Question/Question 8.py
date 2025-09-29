# Q8) Reverse a list using slicing.
# Q9) Sort a list of numbers in ascending order.
# Q10) Sort a list of numbers in descending order order.

import random

students_=[]

for _ in range(10) :
    number=random.randint(1,100000)
    temp=(f'Student{number}')
    if(temp not in students_) :
        students_.append(temp)

print(students_)
# Output ----> ['Student90070', 'Student9681', 'Student62425', 'Student39255', 'Student43482', 'Student37004', 'Student11355', 'Student36652', 'Student77666', 'Student6084']
students_.reverse()
print(students_)
# Output ----> ['Student6084', 'Student77666', 'Student36652', 'Student11355', 'Student37004', 'Student43482', 'Student39255', 'Student62425', 'Student9681', 'Student90070']
students_.sort(reverse=True)
print("Descending Order ",students_)
# output -----> ['Student9681', 'Student90070', 'Student77666', 'Student62425', 'Student6084', 'Student43482', 'Student39255', 'Student37004', 'Student36652', 'Student11355']
students_.sort()
print(students_)
# output ---> ['Student13803', 'Student41631', 'Student45537', 'Student48579', 'Student64725', 'Student88939', 'Student89447', 'Student9291', 'Student94363', 'Student95038']