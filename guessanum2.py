import random
def main():
    lower,upper=0,9
    random_number=random.randint(lower,upper)
    print(f"Guess a number between {lower} and {upper} (you have 10 tries)")
    for attempt in range(10):
        x=int(input(f"Attempt {attempt+1}:Enter your Guess:"))
        if x==random_number:
            print(f"Congrats! {x} is correct. You won!")
            break
        else:
            print("Incorrect Guess.try again!")
            if attempt==9:
                print(f"You've used all attempts. The correct guess was {random_number}.")
main()
