# Write a Python function that takes a list of integers and returns the largest and 2nd largest  numbers in the list

def check(my_list):
    max_1 = 0
    max_2 = 0
    
    for i in my_list:
        if i > max_1:
            max_1 = i
        elif i > max_2:
            max_2 = i
            
    
    print(max_1)    
    print(max_2)    
check([32,13,124,59,86])        