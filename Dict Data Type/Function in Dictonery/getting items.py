d1={1:'Atharv',2:'Parag',3:'Babu',4:'Chatur',5:'Pratiksha',6:'Rajendra',7:'Karan',8:'Tejas'}

print(d1.items())

for item in d1.items():
    print(item)

for k,v in d1.items():
    print(k,'---->',v)
#1 ----> Atharv
#2 ----> Parag
#3 ----> Babu
#4 ----> Chatur
#5 ----> Pratiksha
#6 ----> Rajendra
#7 ----> Karan
#8 ----> Tejas

#Process finished with exit code 0

for k,v in enumerate(d1.items()):
    print(k,'---->',v)
    #0 ----> (1, 'Atharv')
#1 ----> (2, 'Parag')
#2 ----> (3, 'Babu')
#3 ----> (4, 'Chatur')
#4 ----> (5, 'Pratiksha')
#5 ----> (6, 'Rajendra')
#6 ----> (7, 'Karan')
#7 ----> (8, 'Tejas')

# modified Version of the Enumeration
print('--------------------->')
for x in enumerate(d1):
    print(x[0],'---->',x[1],'---->',d1[x[1]])
#--------------------->
#0 ----> 1 ----> Atharv
#1 ----> 2 ----> Parag
#2 ----> 3 ----> Babu
#3 ----> 4 ----> Chatur
#4 ----> 5 ----> Pratiksha
#5 ----> 6 ----> Rajendra
#6----> 7 ----> Karan
#7 ----> 8 ----> Tejas

for x in d1:
    print(x)

#1
#2
#3
#4
#5
#6
#7
#8