x=int(input("Enter a number:"))
if x<=1:
    print("The given number is not a prime number")
else:
    for i in range(2,x):
        if x%i==0:
            print("The given number is not prime.")
            break
    else:
        print("The given number is a prime number.")    