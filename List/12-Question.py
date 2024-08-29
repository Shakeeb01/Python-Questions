# Implement a function that takes a list of numbers and returns a list with the squares of each number.

def square_numbers(my_list):
    new_list = []
    for i in my_list:
       result  =  i * i
       new_list.append(result)
    return new_list

print(square_numbers([2,3,4,5,6,7,8,9]))
    
    