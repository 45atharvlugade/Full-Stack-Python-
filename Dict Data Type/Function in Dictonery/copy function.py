d1={1:'Atharv',2:'Parag',3:'Babu',4:'Chatur',5:'Pratiksha',6:'Rajendra',7:'Karan',8:'Tejas'}


# shallow copy
d2=d1.copy()
print(d1)
print(d2)

# Deep Copy

d3=d1
print(d3)


print('Deep Copy Example after modifying the data ')
d3.update({9:'Shivendra'})
print(d1)
print(d3)