
# Syntax 1 --->

Tuple_=(1,2,3,4,5)

# Syntax 2 ---->
Tuple1_=1,2,3,4,4,5,6,7,8

print(Tuple_,type(Tuple_))
print(Tuple1_,type(Tuple1_))

# converting the string type to the tuple

str1_='Atharv Raghunath Lugade'
tuple2_=tuple(str1_)
print(tuple2_,type(tuple2_))
# Object ----------->    ('A', 't', 'h', 'a', 'r', 'v', ' ', 'R', 'a', 'g', 'h', 'u', 'n', 'a', 't', 'h', ' ', 'L', 'u', 'g', 'a', 'd', 'e') <class 'tuple'>
str2_='Parag kadam'
tuple3_=tuple([str2_])  # stroring in the format of the list
print(tuple3_,type(tuple3_))
# Output -----------> ('Parag kadam',) <class 'tuple'>