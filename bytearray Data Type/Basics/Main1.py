lst=[1,2,3,4,5,6,7,8,9,0]
print(lst , "List ",type(lst))

bytarr=(bytearray(lst))
print(bytarr,"Byte Array ",type(bytarr))

for item in bytarr :
    print(item)

# bytearry is the mutable object .....................}
# it follows the insertion order --------------------->
print("Byte Array Ended Here")
#print(id(bytearray(list)))
