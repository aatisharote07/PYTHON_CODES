with open("students.csv","r") as f:
    for line in f:
        row=line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]} ")


with open("students.csv","r") as f:
    for line in f:
        name,house=line.rstrip().split(",")
        print(f"{name} is in {house} ")