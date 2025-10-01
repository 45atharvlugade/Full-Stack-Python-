# Write a program to remove a particular student’s roll number from the set (if it exists).

rollcalls=set({1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,})

print(rollcalls, len(rollcalls))
rollcalls.discard(1)
print(rollcalls,len(rollcalls))