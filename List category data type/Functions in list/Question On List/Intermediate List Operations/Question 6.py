# Q6) Combine two lists into one.

even_=[]
for i in range(1,51):
    if i % 2==0 :
        even_.append(i)
print(even_)
odd_=[]
for i in range(1,51) :
    if i%2 !=0 :
        odd_.append(i)
print(odd_)

numbers_=odd_+even_
numbers_.sort()
print(numbers_)