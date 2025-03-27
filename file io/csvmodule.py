import csv
students=[]
with open("students.csv","r") as f:
    reader= csv.reader(f)
    for name,home in reader:
        students.append({"name":name,"home":home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
