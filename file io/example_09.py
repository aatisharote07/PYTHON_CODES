with open("copy_text.txt", "r") as f:
    content1=f.read()
with open("text.txt", "r") as f:
    content2=f.read()

if content1==content2:
    print("Yes they are identical.")
else:
    print("no they are not identical.")