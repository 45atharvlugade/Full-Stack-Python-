#  remove all the common elements from both the elements and keep only the unique values in that set

s1=set({2,35,6,8,9,0,100,87,65,4,3})
s2=set({23,45,678,90,98,654,2,35,6,8,9})

s2.difference_update(s1)  # ---> {98, 678, 45, 654, 23, 90}
print(s2)