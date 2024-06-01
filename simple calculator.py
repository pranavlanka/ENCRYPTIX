# Task-2 :Design a simple calculator with basic arithmetic operations.
# Prompt the user to input two numbers and an operation choice.
# Perform the calculation and display the result.
# Function to perform arithmetic operations
def calculate(n1, n2, op):
    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    elif op == '*':
        result = n1 * n2
    elif op == '/':
        result = n1 / n2
    elif op == '^':
        result = n1 ** n2
    else:
        result = "Invalid operation"
    return result

# Get input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter an operation (+, -, *, /, ^): ")

# Perform calculation and display result
result = calculate(num1, num2, operation)
print("Result: ", result)
