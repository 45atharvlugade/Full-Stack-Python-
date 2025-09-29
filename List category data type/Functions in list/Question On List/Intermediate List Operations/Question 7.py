# Q7) Remove duplicate elements from a list.
import random

list_=[]

for _ in range(25) :
    number=random.randint(1,10)
    list_.append(number)
print(list_)
print("1",list_.count(1))
print("2",list_.count(2))
print("3",list_.count(3))
print("4",list_.count(4))
print("5",list_.count(5))
print("6",list_.count(6))
print("7",list_.count(7))
print("8",list_.count(8))
print("9",list_.count(9))
print("10",list_.count(10))

for i in list_ :
    for j in list_ :
        if i==j :
            list_.remove(j)
print(list_)


#import random

# Generate the list
#list_ = []
#for _ in range(25):
#    number = random.randint(1, 10)
#    list_.append(number)

#print("Original list:", list_)

# Remove duplicates (preserve order)
#unique_list = []
#for item in list_:
  #  if item not in unique_list:
 #       unique_list.append(item)

#print("List without duplicates:", unique_list)

# Optional: Count occurrences of each number
#for i in range(1, 11):
#    print(i, list_.count(i))
