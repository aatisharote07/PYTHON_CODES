# Time complexity = O(N^2) Not an optimised version
# Simple Approach 
L = [-2,4,7,-1,6,-11,14,3,-1,-6]
d = {}
for i in range(len(L)):
    subarray = []
    for j in range(i,len(L)):
        subarray.append(L[j])
        d[sum(subarray)] = subarray 
max_val = max(d.keys()) 
for i in d:
    if i == max_val:
        print(d[i],max_val)      
        