# Python programm to count the number of digits in a number
def count_digits(number):
    count = 0
    
    # Handle negative numbers
    number = abs(number)
    
    # Loop until the number is reduced to 0
    while number != 0:
        number = number // 10  # Remove the last digit
        count = count + 1
    
    return count

# Input from the user
num = int(input("Enter the Number: "))
print(count_digits(num))