def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


def main():
    print("=" * 40)
    print("      SIMPLE PYTHON CALCULATOR")
    print("=" * 40)

    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            result = add(num1, num2)
            operator = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            operator = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            operator = "*"
        elif choice == "4":
            result = divide(num1, num2)
            operator = "/"
        else:
            print("Invalid choice! Please select between 1 and 4.")
            continue

        print(f"\nResult: {num1} {operator} {num2} = {result}")

        again = input("\nDo you want to perform another calculation? (y/n): ").lower()

        if again != "y":
            print("\nThank you for using the calculator!")
            break


if __name__ == "__main__":
    main()