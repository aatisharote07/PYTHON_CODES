def power(base,exponent=2):
    return base**exponent
try:
    base=int(input("Enter the Number: "))
    exponent_input=input("Enter the exponent (or press Enter to use default 2: ")
    if exponent_input:
        exponent=int(exponent_input)
    else:
        exponent=2
    print(f"{base} raised to the power of {exponent} is {power(base, exponent)} ")
except ValueError:
    print("Enter a valid number")