# calculate the factorial of a number using a loop

Num = int(input("Enter the number for factorial: "))

factorial = 1 

for i in range(1,Num+1):
    
    factorial = factorial * i

print(factorial)    