t = int(input())           
for i in range(t):
    #Accept 4 integers as input
    X1,Y1,X2,Y2 = map(int, input().split()) 
    if X1+Y1>X2+Y2:
        print(f"{X1+Y1}")
    else:
        print(f"{X2+Y2}")