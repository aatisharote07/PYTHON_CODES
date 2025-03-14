word=input("input a number to reverse: ")
for char in range(len(word)-1,-1,-1):
    print(word[char],end="")
print()