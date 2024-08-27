# Write a function that reverses a string. The input string is given as an array of characters s.

s = ["s","h","a","k","i","b"]

new_str = []

for i in range(len(s)-1,-1,-1):
    new_str.append(s[i])
    
print(new_str)    