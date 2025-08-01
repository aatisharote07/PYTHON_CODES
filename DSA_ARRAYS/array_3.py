# In this question you have to find the subarray which is equal to given sum
# Return the starting and ending index of the subarray 
# Return sub array incase of multiple

# Time complexity O(N^2)
L = [1,22,13,7,9,11,10]
S = 16
for i in range(0,len(L)):
    subarray = []
    for j in range(i,len(L)):
        subarray.append(L[j])
        if sum(subarray) == S:
            print(subarray)

            
# Time Complexity O(N)
d = {}
curr_sum = 0
for i in range(len(L)):
    curr_sum = curr_sum + L[i]
    if (curr_sum - S) in d:
        print(d[curr_sum - S]+1,i)
    d[curr_sum] = i
