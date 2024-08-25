l = [9,56,3,43,4,24,343,60,4]

max = 0
index = 0

max2 = 0
index2 = 0

for i in range(len(l)):
    if l[i] > max:
        max2 = max
        max = l[i]
        index2 = index
        index = i
    elif l[i] > max2:
        max2 = l[i]
        index2 = i    
        

print(f"the Greatest value in a list is {max} and is placed at {index}\nand second greates value is {max2} and is placed at {index2}")  