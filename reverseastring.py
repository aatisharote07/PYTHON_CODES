text = input("Enter the string: ")  

for i in range(len(text) - 1, -1, -1):  # Loop backward
    print(text[i], end="")  # Print characters in reverse order without newline
