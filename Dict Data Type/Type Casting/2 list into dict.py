list1=[1,2,3,4,5,6,7,8,9]
list2=['Atharv','Parag','Babu','Rajesh','Karan','Tejas','Mahesh','Tanmay','Prathmesh']




dict_=zip(list1,list2)   # here dict_ is the object created

for number,name in dict_:
    print(number,name)


d=dict(dict_)
print(d)

for key,value in d.items():
    print(key,value)
