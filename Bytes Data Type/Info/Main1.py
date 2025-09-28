# to store the Sequesntial Data it is used to store
# purpose of the this data type is for the security that is to  perform the encoding and the decoding
# to implement end to end encryption between remote machines
# bytes data types uses the range of values from [0 to 256]
# help(bytes)------> for more information

# Notes------->
#              there is no proper syntax for bytes we need to convert it from one to anothter i.e is type casting
# in python all th data is stored in the form if the object
# Syntax varname=(bytes)(object)
#  object can be iterable and non-iterable
lst=[1,2,3,4,5,6,7,8,9]
print(lst,type(lst))
bts=(bytes)(lst)
print(bts,type(bts))
#
#
#
#
i=10
print(i,bytes(i),type(bytes(i)))


# bytes maintain the insertion order
# we can perform the slicing oepration on bytes data types

# Mutable-----------------------------> vs immutable object ------------------------->
# changes can be done in same                chabges can be done at the same object
# object address                             address
#
#                                            immutable object does not support item assignment
#Example--->list,byteArray,set,dict          Example ----> int,float,string,bytes,range,tuple,frogenset , nonetype
