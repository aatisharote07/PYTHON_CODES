def add_numbers(a,b,c):
    return a+b+c
try:

    a=int(input("Enter the first num: "))
    b=int(input("Enter the second num: "))
    c=int(input("Enter the third num: "))

    print(f"The sum of {a}, {b} and {c} is {add_numbers(a,b,c)}")
except ValueError:
    print("please Enter valid number.")
