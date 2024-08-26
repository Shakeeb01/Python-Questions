# Write a program that takes a list of numbers and prints only the odd numbers using a for loop.

result = []

def odd_nums(my_list):
    for i in my_list:
        if i % 2 != 0:
            result.append(i)

odd_nums([2,3,34,33,80,33,4545,2,2546,565])            

print(result)