def calculator():
    print("\n--- Basic Calculator ---")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input! Please enter numbers.")

    print("\n1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Choose operation: ")

    if choice == "1":
        print("Result:", num1 + num2)

    elif choice == "2":
        print("Result:", num1 - num2)

    elif choice == "3":
        print("Result:", num1 * num2)

    elif choice == "4":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error! Division by zero is not allowed.")

    else:
        print("Invalid operation!")


def km_to_miles():
    while True:
        try:
            km = float(input("Enter distance in KM: "))
            miles = km * 0.621371
            print("Distance in Miles:", round(miles, 2))
            break
        except ValueError:
            print("Please enter a valid number!")


def celsius_to_fahrenheit():
    while True:
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print("Temperature in Fahrenheit:", round(fahrenheit, 2))
            break
        except ValueError:
            print("Please enter a valid number!")


def currency_converter():
    while True:
        try:
            inr = float(input("Enter amount in INR: "))
            rate = float(input("Enter INR value of 1 USD: "))

            if rate <= 0:
                print("Exchange rate must be positive!")
                continue

            usd = inr / rate
            print("Amount in USD:", round(usd, 2))
            break

        except ValueError:
            print("Please enter valid numbers!")


# Main Menu
while True:

    print("\n==============================")
    print(" INTERACTIVE CALCULATOR")
    print("==============================")
    print("1. Basic Calculator")
    print("2. KM to Miles")
    print("3. Celsius to Fahrenheit")
    print("4. INR to USD")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        calculator()

    elif choice == "2":
        km_to_miles()

    elif choice == "3":
        celsius_to_fahrenheit()

    elif choice == "4":
        currency_converter()

    elif choice == "5":
        print("Thank you for using the calculator!")
        break

    else:
        print("Invalid choice! Please select 1 to 5.")
