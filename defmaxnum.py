def find_max(numbers): 
    largest=max(my_list)
    print("Largest number: ", largest)
my_list = [input(f"Enter element {i+1}: ") for i in range(int(input("Enter number of elements: ")))]
print("Your list:", my_list)
find_max(my_list)


    