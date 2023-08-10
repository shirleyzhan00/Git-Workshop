def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def square(a, b):
    return a ** b;

print("Simple Python Calculator")
print("Operations:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponent")

while True:
    choice = input("Enter operation (1/2/3/4/5) or 'exit' to quit: ")

    if choice.lower() == 'exit':
        print("Calculator closed.")
        break

    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid input. Please try again.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)

    elif choice == '5':
        result = square(num1, num2)
    print("Result: ", result)
