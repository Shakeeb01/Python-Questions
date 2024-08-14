#  Count all the letters,digits and special symbols in a given string.

str = "P@#yn26at>&i5ve"

chr = 0
dig = 0
specialChr = 0


for i in str:
    if i.isdigit():
        dig = dig + 1
    elif i.isalpha():
        chr = chr + 1
    else:
        specialChr = specialChr + 1        
        
        
print(chr)        
print(dig)        
print(specialChr)        