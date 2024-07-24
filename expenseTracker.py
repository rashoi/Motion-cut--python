import csv
from datetime import datetime

DATA_FILE = 'expenses.csv'


def add_expense(amount, description, category):

    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), amount, description, category])


def input_expense():

    try:
        amount = float(input("Enter amount spent: "))
        description = input("Enter description: ")
        category = input("Enter category (Food, Transportation, Entertainment): ")

        if category not in ["Food", "Transportation", "Entertainment"]:
            print("Invalid category.")
            return

        add_expense(amount, description, category)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount. Please enter a number.")


if __name__ == "__main__":
    input_expense()
