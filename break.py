
av=5
x=int(input("How many candies do you want? "))
i=1
while i<=x:
    if av<i:
        print("out of stock")
        break
    print("Candy")
    i+=1
print("Bye")