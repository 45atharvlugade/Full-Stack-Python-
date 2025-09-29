# Q5) Insert a value at index 2 in a list.
import random

students_=[]

for _ in range(10) :
    number=random.randint(1,100000)
    temp=(f'Student{number}')
    if(temp not in students_) :
        students_.append(temp)
print(students_)
# ['Student53776', 'Student86356', 'Student57870', 'Student56929', 'Student31014', 'Student52965', 'Student19855', 'Student17050', 'Student99775', 'Student29040']
students_.insert(2,'Atharv Raghunath Lugade')
print(students_)
# ['Student53776', 'Student86356', 'Atharv Raghunath Lugade', 'Student57870', 'Student56929', 'Student31014', 'Student52965', 'Student19855', 'Student17050', 'Student99775', 'Student29040']