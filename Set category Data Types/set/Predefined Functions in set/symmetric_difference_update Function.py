
# this function removes the common elements from both ibje1 and obj2 and takes the remaining elements from both setObj1 and the setObj3 and place them in setObj1 itself
s1=set({1,2,4,7,0,5})
s2=set({2,3,6,8,4,1})

s1.symmetric_difference_update(s2)  # {0, 3, 5, 6, 7, 8}
print(s1)