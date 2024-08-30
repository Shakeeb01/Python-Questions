# Write a Python function that takes a string as input and returns the string reversed without using any built-in reverse methods.

def check(my_str):
    reverse_Str = ''
    for i in range(len(my_str)-1,-1,-1):
        reverse_Str += my_str[i]
        
    print(reverse_Str)    

check("Shakeeb ur Rehman")