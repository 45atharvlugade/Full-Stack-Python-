# Q8) Find the max and min values in a list.
import random

numbers_=[]

for _ in range(50):
    number=random.randint(1,50)
    numbers_.append(number)

print(numbers_)
numbers_.sort()
print(numbers_)

print("Minimum value -----> : ",numbers_[0])
print("Maximum value -----> : ",numbers_[-1])