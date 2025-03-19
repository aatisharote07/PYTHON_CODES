def main():
    X=[]
    while True: 
        try:
            n=int(input("Enter the number of Elements:"))
            if n<=0:
                print("Please Enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input! Please Enter an integer.") 
    for val in range(n):
            while True:
                try:
                    num=int(input(f"Enter number {val+1}: "))
                    X.append(num)
                    break
                except ValueError:
                    print("Invalid input! Please Enter an integer.")
    count=0
    odd_count=0
    for i in range(len(X)):
        if X[i] % 2==0:
            count+=1
        else:
            odd_count+=1
    print(f"Number of even numbers:{count}")
    print(f"Number of odd numbers:{odd_count}")
    
main()