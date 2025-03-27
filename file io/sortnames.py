names=[]
with open("names.txt", "r") as f:
   for line in f:
      names.append(line.rstrip())
for name in sorted(names):      
    print(f"Hello,{name}")  
# pythonic way of sorting
with open("names.txt","r") as f:
    for line in sorted(f):
        print("Hello,",line.rstrip())

    