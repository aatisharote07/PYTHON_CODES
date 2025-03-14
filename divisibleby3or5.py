y=int(input("Enter the number: "))
if y%3==0 and y%5==0:
    print("Number is divisible by 3 and 5 both")
elif  y%5==0:
    print("Number is divisible by 5")
elif y%3==0 :
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 3 as well as 5")