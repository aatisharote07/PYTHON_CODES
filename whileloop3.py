i = 1
while i <= 4:  #Outer loop runs 4 times
    j = 1
    while j <= 5:  # Inner loop runs 5 times
        print("#", end="")  # Print "#" on the same line
        j = j + 1  # Increment j
    
    print()  # Move to a new line after inner loop completes
    i = i + 1  # Increment i