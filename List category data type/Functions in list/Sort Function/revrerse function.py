import random

numbers=[]

for _ in range(100) :
  number = random.randint(1,100)
  if number not in numbers :
      numbers.append(number)

print(numbers)

numbers.reverse()
print(numbers)