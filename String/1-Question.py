# Print the string in reverse.

a = "shakeeb"

char = ""

for i in range(len(a)-1,-1,-1):
    char = char + a[i]
    
print(char)    


# this is the short way to print any string in reverse.
# print(a[::-1])