new_List=[0,1]

for i in range(2,50):
    next_value= new_List[-1]+new_List[-2]
    new_List.append(next_value)
print(len(new_List))


n = int(input("Enter the number of terms: "))

a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b  # Swap values












