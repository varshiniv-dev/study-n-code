a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
result = float(input(
    "Enter 1 for addition\n 2 for subtraction\n 3 for division\n 4 for multiplication\n:"))
if result == 1:
    addition = a+b
    print("Result:", addition)
elif result == 2:
    subtraction = a-b
    print("Result:", subtraction)
elif result == 3:
    division = a/b
    if b == 0:
        print("Result:", division)

elif result == 4:
    multiplication = a*b
    print("Result:", multiplication)
else:
    print("Invalid input!")
