# sort the list.

l = [1,2,3,4,5]

for i in range(len(l)-1):
    if l[i] <= l[i+1]:
        continue
    
    else:
        print("Your list is not sorted.")
        break
else:
    print("Your list is sorted")    