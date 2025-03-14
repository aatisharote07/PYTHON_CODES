rows = 4  # Number of rows
for i in range(rows):  
    for j in range(i + 1):  
        print(chr(97 + j), end=" ")  # Convert ASCII to character (a, b, c, d)
    
    for k in range(i + 1, rows):  
        print(chr(112 + k - i - 1), end=" ")  # Convert ASCII to character (p, q, r)
    
    print()  # Move to the next line
    