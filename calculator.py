# ===== SMART CALCULATOR MINI PROJECT =====

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b


while True:
    print("\n===== SIMPLE CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Exit")

    choice = input("Choose operation (1-7): ")

    if choice == '7':
        print("Thank you for using calculator ❤️")
        break

    if choice in ['1','2','3','4','5','6']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))

        elif choice == '2':
            print("Result:", subtract(num1, num2))

        elif choice == '3':
            print("Result:", multiply(num1, num2))

        elif choice == '4':
            print("Result:", divide(num1, num2))

        elif choice == '5':
            print("Result:", modulus(num1, num2))

        elif choice == '6':
            print("Result:", power(num1, num2))

    else:
        print("Invalid choice. Please try again.")
