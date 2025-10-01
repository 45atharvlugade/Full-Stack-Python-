s1=set({1,2,3,4,5,6,7,8})
s2=set({6,7,8,0,9})
s3=set({11,22,33,44,55})
s4=set({1,2,3})
s5=set({11})


print(s1.issuperset(s4))
print(s2.issuperset(s4))
print(s3.issuperset(s3))
print(s4.issuperset(s1))
print(s5.issuperset(s1))