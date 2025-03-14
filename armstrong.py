def is_armstrong(number):
    digits=[int(digit) for digit in str(number)]
    num_digits = len(digits)
    armstrong_sum = sum(digit**num_digits for digit in digits)
    return armstrong_sum  ==  number
num=int(input("Enter the Number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number. ")
else:
    print(f"{num} is not an Armstrong number. ")