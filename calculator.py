def calculator():
    print("🧮 Modern Calculator")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /, **, %, //): ").strip()
            num2 = float(input("Enter second number: "))

            operations = {
                "+": lambda a, b: a + b,
                "-": lambda a, b: a - b,
                "*": lambda a, b: a * b,
                "/": lambda a, b: a / b if b != 0 else "Cannot divide by zero!",
                "**": lambda a, b: a ** b,
                "%": lambda a, b: a % b if b != 0 else "Cannot divide by zero!",
                "//": lambda a, b: a // b if b != 0 else "Cannot divide by zero!",
            }

            result = operations.get(operator)

            if result:
                print(f"Result: {result(num1, num2)}")
            else:
                print("Invalid operator!")

        except ValueError:
            print("Please enter valid numbers!")

        choice = input("\nDo you want another calculation? (y/n): ").lower()
        if choice != "y":
            print("👋 Thanks for using the calculator!")
            break


if __name__ == "__main__":
    calculator()