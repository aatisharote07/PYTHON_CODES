x=int(input("Enter a Number: "))
if x < 0:
    print("Factorial is not defined for negative numbers.")
elif x == 0:
    print("Factorial: 1")  
else:
    fact=1
    for i in range(1,x+1):
        fact=fact*i
    print("Factorial:",fact)