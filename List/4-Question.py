l = [9,56,3,43,4,24,343,4]

maxVal = 0
index = 0

for i in range(len(l)):
    if l[i] > maxVal:
        maxVal = l[i]
        index = i
        
        

print(f"the maximum value in a list is {maxVal} and is placed at {index}")        