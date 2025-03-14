x = int(input("Enter the Marks: ")) 
if x<0:
    print("invalid Marks")
if x >= 95:
    print("Grade: A")
    print("Congratulations, You have achieved a scholarship!")
elif x >= 90:
    print("Grade: A")
elif x >= 80:
    print("Grade: B")
elif x >= 70:
    print("Grade: C")
elif x >= 60:
    print("Grade: D")
else:
    print("FAIL")
