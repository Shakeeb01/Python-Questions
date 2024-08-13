# Write a Python program to print the multiplication table of a given number using a loop.

n = int(input("Enter the number for multiplication table: "))

length = int(input("What should be length of the table: "))

for i in range(1,length+1):
    print(f"{n} x {i} = {n * i}")
    