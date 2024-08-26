# Write a program that prints the characters at even indexes from a given string using a for loop.


my_str = "Conditionals"
#         
for i, char in enumerate(my_str,start=0):
    if i % 2 == 0:
        print(i,char)
    else:
        continue
        
    