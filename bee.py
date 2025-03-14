WORDS={"PAIR":4,"HAIR":4,"CHAIR":5,"GRAPHIC":7 }
def main():
    print("Welcome to spelling bee!")
    print("Your letters are: A I P C R H G")
    
    while len(WORDS)>0:
        print(f"{len(WORDS)} words left!")
        guess=input("Guess the word: ").upper()
        if guess=="GRAPHIC":
            points = WORDS.pop(guess)  
            print(f"Good job! You scored {points} points.")
            WORDS.clear()  
            print("You've won!")
            

            if guess in WORDS.keys():
                points= WORDS.pop(guess)
                print(f"Good job! You scored {points} points.")
        else:
            print("Incorrect, Try again!")
        
    print("Thats the game!")    
main()