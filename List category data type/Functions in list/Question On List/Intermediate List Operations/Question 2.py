# Q2) Count how many times a value appears in a list.
import random

list_=[]

for _ in range(100) :
    number=random.randint(1,10)
    list_.append(number)
print(list_)

print(list_.count(1))
print(list_.count(2))
print(list_.count(3))
print(list_.count(4))
print(list_.count(6))

# for String

str1='Atharv Raghunath Lugade'
print(str1.count('a'))

# output---------------------->

# [2, 5, 8, 3, 4, 10, 1, 1, 2, 10, 1, 9, 10, 3, 4, 8, 7, 6, 10, 8, 4, 2, 3, 9, 3, 6, 4, 9, 1, 6, 5, 6, 10, 9, 9, 7, 2, 6, 4, 4, 10, 3, 2, 4, 1, 3, 7, 4, 7, 9, 1, 8, 9, 10, 1, 9, 7, 9, 8, 7, 8, 5, 5, 10, 5, 10, 10, 10, 5, 8, 8, 4, 4, 9, 10, 7, 1, 1, 5, 7, 1, 8, 2, 5, 8, 2, 2, 10, 1, 6, 7, 9, 2, 7, 9, 7, 10, 6, 9, 10]
# 11
# 9
# 6
# 10
# 7
# 4
