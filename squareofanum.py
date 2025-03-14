num=int(input("Enter a number: "))
if num<0:
     print("Cannot take square from 1 to a negative number.")
elif num==0:
    print("Square of 0 is always zero")     
else:     
    for i in range (1,num+1):
        print(i**2,end=" ")
print()    