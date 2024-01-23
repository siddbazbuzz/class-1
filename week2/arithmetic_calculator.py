
import math

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

operation = input("Enter the arithmetic operation (+, -, *, /): ")


if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero")
        exit()
else:
    print("Error: Invalid operation")
    exit()


print(f"\nThe result of {num1} {operation} {num2} is: {result}")
 