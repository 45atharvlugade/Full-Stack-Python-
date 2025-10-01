

# Delta Operations -------------------->
set1=set({1,2,3,4,5})
set2=set({9,8,7,6,5,4})
print(set1.symmetric_difference(set2)) # ------------> {1, 2, 3, 6, 7, 8, 9}
print(set2.symmetric_difference(set1)) # ------------> {1, 2, 3, 6, 7, 8, 9}