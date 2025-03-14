def greet():
    print("Hello!")
    for i in range(4):
        for j in range(4):
            print("#",end="")
        print()    
greet()    
print("My name is Aatish")
def many_types(x):
    if x<0:
        return("Hello Aatish")
    else:
        return 0
print(many_types(1))
print(many_types(-1))