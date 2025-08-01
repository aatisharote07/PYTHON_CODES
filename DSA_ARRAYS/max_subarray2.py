# Time Complexity is O(N)
# More Optimised solution
L = [-2,4,7,-1,6,-11,14,3,-1,-6]

curr_sum = 0
curr_seq = []
best_sum = L[0]
best_seq = []

for i in L:
    if i + curr_sum > i:
        curr_sum = curr_sum + i
        curr_seq.append(i)
    else:
        curr_sum = i
        curr_seq.clear()
        curr_seq.append(i)
    if curr_sum > best_sum:
        best_sum =  curr_sum
        best_seq = curr_seq
print(best_sum,best_seq)        