tuple_=(1,2,3,4,5,(2,3,4,5,5,(2,3,4,5,6,6,)),34)
print(tuple_)
print(type(tuple_))
print(len(tuple_))
print(tuple_[5])
print(type(tuple_[5]))
print(tuple_[5][1:3])

#(1, 2, 3, 4, 5, (2, 3, 4, 5, 5, (2, 3, 4, 5, 6, 6)), 34)
#<class 'tuple'>
#7
#(2, 3, 4, 5, 5, (2, 3, 4, 5, 6, 6))
#<class 'tuple'>
#(3, 4)
