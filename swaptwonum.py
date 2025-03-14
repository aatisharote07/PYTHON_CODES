a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
print(f"Orignal values: a={a}, b={b}")
a,b=b,a
print(f"Swapped values: a={a}, b={b}")