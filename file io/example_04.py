words=["donkey","cringe","garbage","lol"]

with open("sample.txt","r") as f:
    content=f.read()
content_new = content.replace(words,"######")
with open("sample.txt","w") as f:
    f.write(content_new)
    
        