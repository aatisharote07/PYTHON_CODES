text = input("Enter a string: ")  # Take input from the user
vowels = "aeiouAEIOU"  # Define vowels (both lowercase and uppercase)
count = 0  # Initialize vowel count

for char in text:  # Iterate through each character in the string
    if char in vowels:  # Check if the character is a vowel
        count += 1  # Increment the count

print("\nVowel count:", count)  # Print the total count of vowels
