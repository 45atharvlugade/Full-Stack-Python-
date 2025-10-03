d1={
    1:'Atharv',
    2:{1:'Parag',2:990028383},
    3:{5:{7:'22.27',4:'atharv'},6:'Maharani'}
}

print(d1[2][2])   # ---> 990028383
print(d1[2][1])   #----->Parag
print(d1[3][5],type(d1[3][5]))

for key , value in d1[3][5].items() :
    print(key,value)

d1[3][5].update({9:'Mp'})
print(d1[3][5])