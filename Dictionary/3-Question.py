# count the frequency of each elements in list.

a = [1,2,4,2,1,4,2,4,6,6,7,73,2,5,5,5,2]

dict = {}

for i in a:
    if i in dict.keys(): # this will check if there is any key in dict equal to index of a.
        dict[i] = dict[i] + 1   # this will increment the count of the value.
    else:
        dict[i] = 1     # this will create the key in the dictionary.
        
        
print(dict)       


# this is count the frequency of each elements in str.
str = "Shakeeb ur Rehman"

dict = {}

for i in str:
    if i in dict.keys():
        dict[i] = dict[i] + 1
    else:
        dict[i] = 1

print(dict)            