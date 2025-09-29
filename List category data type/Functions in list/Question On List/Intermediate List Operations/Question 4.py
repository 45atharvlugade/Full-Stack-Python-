# Q4) Use list comprehension to create a list of squares from 1 to 10.

square_=[]
count=0
for i in range(100+1) :
    count+=1
    square_.append(i**3)
print(square_)
print('Count : ',count)
