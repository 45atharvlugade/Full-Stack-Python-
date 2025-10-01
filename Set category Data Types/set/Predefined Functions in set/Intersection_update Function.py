# this function will take the common elements from Object 1 and Object 2 and keep them in any 1 or 2 object Object as per the syntax

s1=set({1,2,3,4,78,9,})
s2=set({34,5,6,2,1,9})

s1.intersection_update(s2)   # {1, 2, 9}
print(s1)