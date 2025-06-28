# Simple CLI Calculator by Droo

a = int(input("Enter first number: "))
operator = input("Select operator (+ - * /): ")
b = int(input("Enter second number: "))

if operator == '+':
    print("Result:", a + b)
elif operator == '-':
    print("Result:", a - b)
elif operator == '*':
    print("Result:", a * b)
elif operator == '/':
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator selected.")
