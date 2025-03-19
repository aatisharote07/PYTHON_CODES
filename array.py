from numpy import *
vals= array([33,4,5,73,56])
del vals[1]
print(vals) 
nums=array([])    
for i in range(len(vals)-1,-1,-1):
    nums.append(vals[i])
print(nums)     