def factorial(x):
    if x<0:
        return "Factorial is not defined for negative numbers."
    elif x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
x=int(input("Enter the number: "))
print(f"Factorial of {x} is {factorial(x)}")