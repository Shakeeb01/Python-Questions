# write the python programm to combine two dictionaries by adding values for commom keys.
a = {
    1:10,
    2:20,
    3:40,
}
b = {
    4:40,
    5:50,
    6:60,
    2:50
}

for i in b.keys():
    if i in a.keys():
        a[i] = a[i] + b[i]
    else:
        a[i] = b[i]
        
        
print(a)            