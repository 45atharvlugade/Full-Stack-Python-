# represents the string data
name='Atharv'
age=20
percentage=99.99

print('%s have age if %d and got the percentage of : %f'%(name,age,percentage))

list_=[name,age,percentage]
#print('---->%d'%list_)
#Traceback (most recent call last):
#  File "D:\Full Stack Python\Displaying the Result of Python on Console\print Function\Formar specifiers\%s.py", line 9, in <module>
 #   print('---->%d'%list_)
#          ~~~~~~~~~^~~~~~
#TypeError: %d format: a real number is required, not list
print('---->%s'%list_)   # ---> ['Atharv', 20, 99.99]

# for dict

dict_={1:name,2:age,3:percentage}
print('---->%s , type of dict is %s'%(dict_,type(dict_)))