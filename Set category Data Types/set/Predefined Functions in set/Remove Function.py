names_=set({'Atharv','Parag','Babu','Prathmesh','Tejas'})
print(names_,type(names_))

# names_.remove('babu') -----> KeyError: 'babu'
#print(names_)
#names_.remove('Babu')
#print(names_)

#output--------->

#
#{'Parag', 'Prathmesh', 'Babu', 'Atharv', 'Tejas'} <class 'set'>
#{'Parag', 'Prathmesh', 'Babu', 'Atharv', 'Tejas'}
#{'Parag', 'Prathmesh', 'Atharv', 'Tejas'}

numbers_=set({1,2,3,4,56,7,8,9,})
print(numbers_ , type(numbers_))
numbers_.remove(1000)
print(numbers_)

#OUTPUT--------------------------------->

# numbers_.remove(1000)
#KeyError: 1000
