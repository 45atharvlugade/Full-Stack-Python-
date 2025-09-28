import random
numbers=[]

for _ in range(1,1000) :
    number=random.randint(1,10000)
    if( number not in numbers) :
        numbers.append(number)
print(numbers)
numbers.sort(reverse=False)
print(numbers)