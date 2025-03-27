students=[]
with open("students.csv","r") as f:
    for line in f:
        name,house=line.rstrip().split(",")
        students.append(f"{name} is in {house}")
for student in sorted(students):
    print(student)
# pythonic way of sorting students or their respected houses using dictionaries
students=[]
with open("students.csv","r") as f:
    for line in f:
        name,house=line.rstrip().split(",")
        student={"name": name,"house": house}
        students.append(student)
def get_name(student):
    return student["name"]
for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}" )   
## another pythonic way of sorting students or their respected houses using dictionaries
#  and using a lamda function(anonymous) function
students=[]
with open("students.csv","r") as f:
    for line in f:
        name,house=line.rstrip().split(",")
        student={"name": name,"house": house}
        students.append(student)
for student in sorted(students, key=lambda student:student["name"]):
    print(f"{student['name']} is in {student['house']}")