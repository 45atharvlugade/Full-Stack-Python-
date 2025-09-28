
students=[100,"Atharv Raghunath Lugade",15000.00,"Kolhapur",2+3j]  # Nonempty List
print(type(students))
print(students)

teacher=[] # EMpty List

#  on the olist we can perform the operations on it
print(students[0:4])
print()

numbers=[-1,2,3,4,-3,-8,9,7,-7]

negative_list=[]
positive_list=[]

for num in numbers :
    if num >=0 :
        positive_list.append(num)
    if(num <=0 ) :
        negative_list.append(num)

print(positive_list)
print("---------------------------")
print(negative_list)

# converting one list to anotehr list
# temp1_list=list as positive_list
temp_list=(list)(positive_list)
print(type(temp_list))


# list to int conversion is not possible
# i.e.

# list_1=(list)(10) ---> conversion is not possible
# print(type(list_1))
#
# ----> Traceback (most recent call last):
#   File "D:\Full Stack Python\List category data type\Basics\Main2.py", line 36, in <module>
#     list_1=(list)(10)
#            ^^^^^^^^^^
# TypeError: 'int' object is not iterable


print('I m here =1 ---->',temp_list[4])  # ----> { only iterable objects can be converted to list }
