
myList = [1,2,3,5,3,2,1]

newList = []

for i in range(len(myList)-1,-1,-1):
    newList.append(myList[i])


if newList == myList:
    print("Your list is Palindrome")
else:
    print("Your list is not palindrome")     
    
    