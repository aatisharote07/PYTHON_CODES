def main():
    names=["Mario","Luigi","Daisy","Yoshi","Aatish"]
    for name in names:
        print(write_letter(name,"Princess peach"))
def write_letter(receiver, sender):
    return  f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    Dear {receiver},

    You are cordially invited to a ball 
    Peache's Castle this evening, 7:00PM.
    Sincerely,
    {sender}  
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """
main()  
