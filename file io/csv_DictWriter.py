import csv  
name=input("What's your name?: ")
house=input("What's your house?: ")
 
with open("Students_new.csv","a") as f:
    writer=csv.DictWriter(f,fieldnames=["name","house"])
    writer.writerow({"name":name,"house":house})