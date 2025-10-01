s1=set({1,2,3,5})
s2=set({9,3,6,5})

s3=s1.update(s2)
s2.update(s1)
print(s3)  #-----> None

print(s1,id(s1))
print(s2,id(s2))
#{1, 2, 3, 5, 6, 9} 1508517814432
#{1, 2, 3, 5, 6, 9} 1508517815328

# only different values are added

s4=set({1,2,3,4})
s5=set({1,2,3,4})

s4.update(s5)
print(s4)

# this Function is used for adding and merging the values of Obj1 with Obj2
