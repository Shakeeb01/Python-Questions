# Check if a string is palindrome or not.

a = "rotator"

b = ''

for i in range(len(a)-1,-1,-1):
    b = b + a[i]
    
if a == b:
    print(f" '{a}' is a palindrome")
else:
    print(f" '{a}' is not  palindrome")        