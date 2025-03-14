name=input("What's your name: ")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffinor")
    case "draco":
        print("Slytherin")
    case _:
        print("Who?")