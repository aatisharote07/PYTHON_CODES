rows = 7
cols = 5

for i in range(rows):
    for j in range(cols):
        if (
            (j == 0 or j == cols - 1) and i != 0  # Vertical sides
            or (i == 0 and j in range(1, cols - 1))  # Top horizontal line
            or i == rows // 2  # Middle horizontal line
        ):
            print("*", end="")
        else:
            print(" ", end="")
    print() 
'''
 *** 
*   *
*   *
*****
*   *
*   *
*   *
'''