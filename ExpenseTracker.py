import json
from datetime import datetime

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []
    return expenses

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=2)

def add_expense(expenses, amount, category):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expenses.append({"timestamp": timestamp, "amount": amount, "category": category})
    save_expenses(expenses)
    print("Expense added successfully.")

def view_expenses(expenses):
    print("\nExpense Summary:")
    if not expenses:
        print("No expenses recorded.")
    else:
        for expense in expenses:
            print(f"{expense['timestamp']} - ${expense['amount']} ({expense['category']})")

def view_spending_pattern(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    categories = {}
    for expense in expenses:
        category = expense["category"]
        amount = float(expense["amount"])
        categories[category] = categories.get(category, 0) + amount

    print("\nSpending Pattern:")
    for category, amount in categories.items():
        print(f"{category}: ${amount:.2f}")

def main():
    expenses = load_expenses()

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. View Spending Pattern")
        print("4. Quit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            amount = float(input("Enter the expense amount: $"))
            category = input("Enter the expense category: ")
            add_expense(expenses, amount, category)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_spending_pattern(expenses)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
