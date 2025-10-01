s1=set({1,2,3,4,5,6,7,8})
s2=set({6,7,8,0,9})
s3=set({11,22,33,44,55})


# Disjoint ----------> No common elements
#          ----------> Boolean Function ---> True/False
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))
print(s2.isdisjoint(s3))

# Important Question ------------->

print(set().isdisjoint(set()))  #----------> True
print(set().isdisjoint(set({10,20,30})))  #----------> True
print(set().isdisjoint(set({1})))   # ---------> True

