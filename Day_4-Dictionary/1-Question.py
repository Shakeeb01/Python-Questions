#  Write the python script to merge two dictionaries

a = {
    1:10,
    2:20,
    3:40,
}



b = {
    4:40,
    5:50,
    6:60,
}

a.update(b)
print(b) 

# if there are some same keys in both the dictionaries then there values will be updated also.