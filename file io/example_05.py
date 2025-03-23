words=["donkey","cringe","garbage","lol"]

with open("sample.txt","r") as f:
    content=f.read()

for word in words:
    content = content.replace(word,"#"*len(word))
with open("sample.txt","w") as f:
    f.write(content)
    
