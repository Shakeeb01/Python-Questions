# Create a function that removes all the duplicate elements from a given list without using any built-in functions.

def check_duplicate(my_list):
    unique_list = []
    
    for item in my_list:
        if item not in unique_list:
            unique_list.append(item)
    
    
    print(unique_list)
    
    
check_duplicate([2,6,2,6,9,2,5,1])            