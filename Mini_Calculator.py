# Simple Calculator Program

# Ask the user to enter the first number
num1 = float(input("3: "))

# Ask the user to enter the second number
num2 = float(input("2: "))

# Ask the user to enter a mathematical operation
operation = input("Enter an operation (+ for addition, - for subtraction, * for multiplication, / for division): ")

# Perform the calculation based on the user's input
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation. Please use +, -, *, or /.")
