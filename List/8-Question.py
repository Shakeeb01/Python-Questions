# Write a function that reverses a string. The input string is given as an array of characters s.

s = ["s","h","a","k","i","b"]

left, right = 0, len(s)-1


while left < right:
    # Swap characters at positions left and right
    s[left], s[right] = s[right], s[left]
    # Move the pointers towards the center
    
    left += 1
    right -= 1
    
print(s)    


    
   