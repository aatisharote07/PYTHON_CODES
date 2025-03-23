with open("text.txt", "r") as f:
    content=f.read()
with open("Copy_text.txt","w") as f:
    f.write(content)