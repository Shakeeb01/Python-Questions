# Count vowels in a given string.

def VowelCheck(str):
    # Vowels
    Allvowels = "aeiouAEIOU"

    # Vowels Count
    VowelCount = 0
    constCount = 0
    for char in str:
        if char in Allvowels:
          VowelCount = VowelCount + 1
        else:
            constCount = constCount + 1
    print(VowelCount)        
    print(constCount)        
    
VowelCheck("Shakeeb")    
