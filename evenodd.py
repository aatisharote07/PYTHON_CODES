x=int(input("Enter a number:"))
r=x%2
if r==0:
    print("Even")
    if x>5:
        print("x is great")
    else: 
        print("x is not so great")
else:
    print("Odd")