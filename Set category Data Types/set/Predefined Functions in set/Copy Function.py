number1_=set({1,2,3,4,5,6})
number2=number1_ # Deep Copy
print(number2)

number2.add(100)

print(number1_)
print(number2)


print("SHALLOW COPY")

number3=set({1,2,3,4,5,6,7,8})
number4=number3.copy()
print(number3)
print(number4)

number4.add(111)
print(number3)
print(number4)
