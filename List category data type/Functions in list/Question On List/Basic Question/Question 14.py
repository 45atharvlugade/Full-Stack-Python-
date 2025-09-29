# Q14) Check if a value exists in a list.

number_=[1,2,3,4,5,6,7,8,9]

for i in number_ :
    if 9 in number_ :
        print('Found')
        print(number_.index(9))
        break
    else :
        print('Not Found ')
