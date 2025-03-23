with open ("log.txt") as f:
    content=f.read()
words=["Technology","internet","infromation","security"]

if any (word in content for word in words):
    print("Yes the words-'Technology','internet','information','security' are present in the content.")
else:
    print("No the words are not present in the content.")
