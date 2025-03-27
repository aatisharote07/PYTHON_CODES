import csv
l1=[]
count=0
with open("students.csv", "r") as f:
    reader=csv.reader(f) 
    for row in reader:
        l1.append(row)
        count+=1
print(l1[1:])
print(l1[0])
print(count)