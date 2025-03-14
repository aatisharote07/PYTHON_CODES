import random
def main():

    for i in range(10):
        x=int(input("Guess a number between 0 to 9: "))
        if x==random.randrange(10):
            print(f"{x} Your guess was correct")
        else:
            print("Your guess is incorrect!")
            print("Try again")

main()