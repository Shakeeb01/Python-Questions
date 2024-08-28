# Implement a function that takes two lists and returns a list containing only the common elements between them.

def check_common_elems(l1,l2):
    main_list = []
    
    for item in l1:
        if item in l2:
            main_list.append(item)
            
    return  main_list      
    
    
print(check_common_elems([9,5,7,2,5,3],[3,10,13,2,90,7,2]))