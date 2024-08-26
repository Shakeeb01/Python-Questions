# Write a program that prints all the numbers divisible by 5 and 7 within a range of 1 to 100.


div_5 = []  # this will contain all the numbers that will divisible  by 5.
div_7 = []  # this will contain all the numbers that will divisible  by 7.


# For Loop that will run from 1 to 100.
for i in range(1,101):
    if i % 5 == 0:
        div_5.append(i)
    elif i % 7 == 0:
        div_7.append(i)
     
        

print(div_5)        
print(div_7)        