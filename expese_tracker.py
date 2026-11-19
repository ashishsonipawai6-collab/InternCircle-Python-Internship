import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"


# Create CSV file if it does not exist
def create_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])


# Add Expense
def add_expense():
    print("\n--- ADD EXPENSE ---")

    while True:
        date = input("Enter date (YYYY-MM-DD): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date! Use YYYY-MM-DD format.")

    category = input("Enter category: ").strip()

    while not category:
        print("Category cannot be empty!")
        category = input("Enter category: ").strip()

    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero!")
                continue

            break

        except ValueError:
            print("Please enter a valid amount!")

    description = input("Enter description: ").strip()

    with open(FILENAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!")


# View All Expenses
def view_expenses():
    print("\n--- ALL EXPENSES ---")

    with open(FILENAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        expenses = list(reader)

    if not expenses:
        print("No expenses found!")
        return

    for expense in expenses:
        print(
            expense["Date"],
            "|", expense["Category"],
            "| Rs.", expense["Amount"],
            "|", expense["Description"]
        )


# Filter Expenses
def filter_expenses():
    print("\n--- FILTER EXPENSES ---")

    category = input("Enter category to filter: ").strip().lower()

    with open(FILENAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        found = False

        for expense in reader:
            if expense["Category"].lower() == category:
                print(
                    expense["Date"],
                    "|", expense["Category"],
                    "| Rs.", expense["Amount"],
                    "|", expense["Description"]
                )
                found = True

        if not found:
            print("No expenses found in this category!")


# Category Summary
def category_summary():
    print("\n--- CATEGORY SUMMARY ---")

    totals = {}

    with open(FILENAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            category = expense["Category"]
            amount = float(expense["Amount"])

            totals[category] = totals.get(category, 0) + amount

    if not totals:
        print("No expenses available!")
        return

    grand_total = 0

    for category, total in totals.items():
        print(category, ": Rs.", round(total, 2))
        grand_total += total

    print("-----------------------")
    print("Total Expenses: Rs.", round(grand_total, 2))


# Main Menu
create_file()

while True:

    print("\n==============================")
    print(" PERSONAL EXPENSE TRACKER")
    print("==============================")

    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Filter Expenses")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        filter_expenses()

    elif choice == "4":
        category_summary()

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please select 1 to 5.")
