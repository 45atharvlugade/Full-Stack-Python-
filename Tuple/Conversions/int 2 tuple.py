a=10

#tuple1_=tuple(a,) or tuple(a)
#--------------->
# Traceback (most recent call last):
#   File "D:\Full Stack Python\Tuple\Conversions\int 2 tuple.py", line 3, in <module>
#     tuple1_=tuple(a)
#             ^^^^^^^^
# TypeError: 'int' object is not iterable

# so to overcome the further error we should go for the following error

tuple_=tuple((a,))
print(tuple_,type(tuple_))
#Putput----------->    (10,) <class 'tuple'>