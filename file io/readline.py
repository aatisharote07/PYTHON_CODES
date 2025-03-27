with open("Copy_text.txt","r") as f:    content=f.readlines()
for line in content:
    print(f"Hello,{content}")
    break
# pythonic way to do the same
#with open("Copy_text.txt","r") as f:
#    for line in f:
 #       print("hello",line.rstrip())    