#  write the python programm to sum all the values of dictionary.

a = {
    1:10,
    2:20,
    3:40,
}

sum  = 0

for i in a.values():
    sum = sum + i
    
    
print(sum)