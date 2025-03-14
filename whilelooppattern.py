rows = 5  # Number of rows
i = 1  # Outer loop variable

while i <= rows:  # Controls the number of rows
    j = 1  # Inner loop variable
    while j <= i:  # Prints numbers from 1 to i
        print(j, end=" ")  # Print numbers in the same line
        j += 1
    print()  # Move to the next line after each row
    i += 1  # Increment the row count