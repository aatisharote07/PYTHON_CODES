from numpy import *

vals = array([33, 4, 5, 73, 56])

# Use numpy.delete() instead of del
vals = delete(vals, 1)  # Removes the element at index 1

# Use a Python list for nums
nums = []
for i in range(len(vals)-1, -1, -1):
    nums.append(vals[i])

# Convert back to NumPy array (if needed)
nums = array(nums)

print(nums)
