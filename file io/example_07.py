

with open ("log.txt") as f:
    lines = f.readlines()
lineno=1
for line in lines:
    if("information" in line):
        print(f"Yes information is present.line no: {lineno}")
        break       
    lineno +=1  
else:
    print("no information is not present ")


