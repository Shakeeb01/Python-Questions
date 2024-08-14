
Main_List = [4,6,878,35,-345,-353,53,-353535,-45,34,-53,453,-45,]

PositiveValues = []
NegativeValues = []

for i in Main_List:
    if i > 0:
        PositiveValues.append(i)
    elif i < 0:
        NegativeValues.append(i)    
        
        
        
print(PositiveValues)        
print(NegativeValues)        