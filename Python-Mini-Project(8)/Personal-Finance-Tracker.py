'''                                    PROJECT 7 - PERSONAL FINANCE TRACKER 
                Concepts used: Classes, Objects, Encapsulation, __init__, methods, file handling (JSON)                             '''

import json   # used to save/load transactions in a .json file
import os     # used to check if the save file already exists
from datetime import date  # used to auto-record the date of each transaction

FILE_NAME = "transactions.json"  # file where all transactions will be stored permanently


class Transaction:
    """
    This class represents ONE transaction (either income or expense).
    Think of it as a blueprint for a single money entry.
    """

    def __init__(self, t_type, category, amount, note, t_date=None):
        # t_type will be "income" or "expense"
        self.t_type = t_type
        self.category = category      # e.g. "Food", "Salary", "Rent"
        self.amount = amount          # how much money
        self.note = note              # short description
        # If no date is given, use today's date automatically.
        self.date = t_date if t_date else str(date.today())

    def to_dict(self):
        # Converts the Transaction object into a dictionary.
        # JSON files can only store dictionaries/lists, not Python objects directly.
        return {
            "t_type": self.t_type,
            "category": self.category,
            "amount": self.amount,
            "note": self.note,
            "date": self.date,
        }

    def __str__(self):
        # This special method controls what gets printed
        # when we do print(transaction_object).
        sign = "+" if self.t_type == "income" else "-"
        return f"[{self.date}] {self.t_type.upper():7} | {self.category:12} | {sign}{self.amount:<10} | {self.note}"


class FinanceTracker:
    """
    This class manages MANY Transaction objects.
    It stores them in a list and provides methods to
    add, view, calculate balance, and filter transactions.
    """

    def __init__(self):
        # self.transactions is a list that will hold Transaction objects.
        self.transactions = []
        # As soon as the tracker is created, load any
        # previously saved transactions from the file.
        self.load_transactions()

    def add_transaction(self, t_type, category, amount, note):
        # Step 1: Create a new Transaction object.
        new_txn = Transaction(t_type, category, amount, note)
        # Step 2: Add that object to our transactions list.
        self.transactions.append(new_txn)
        # Step 3: Save the updated list to the file so it's not lost.
        self.save_transactions()
        print(f"{t_type.capitalize()} of {amount} added successfully.\n")

    def view_transactions(self):
        # If the list is empty, there is nothing to show.
        if not self.transactions:
            print("No transactions found.\n")
            return

        print("\n--- ALL TRANSACTIONS ---")
        # enumerate() gives us both the index (i) and the transaction object.
        for i, txn in enumerate(self.transactions, start=1):
            print(f"{i}. {txn}")  # this uses __str__ from Transaction class
        print()

    def view_by_type(self, t_type):
        # This creates a new list containing only transactions
        # that match the given type ("income" or "expense").
        filtered = [t for t in self.transactions if t.t_type == t_type]

        if filtered:
            print(f"\n--- {t_type.upper()} TRANSACTIONS ---")
            for t in filtered:
                print(t)
            print()
        else:
            print(f"No {t_type} transactions found.\n")

    def get_balance(self):
        # sum() adds up amounts using a generator expression.
        total_income = sum(t.amount for t in self.transactions if t.t_type == "income")
        total_expense = sum(t.amount for t in self.transactions if t.t_type == "expense")
        balance = total_income - total_expense
        return total_income, total_expense, balance

    def show_summary(self):
        income, expense, balance = self.get_balance()
        print("\n--- SUMMARY ---")
        print(f"Total Income  : {income}")
        print(f"Total Expense : {expense}")
        print(f"Balance       : {balance}\n")

    def delete_transaction(self, index):
        # index comes from the numbered list shown in view_transactions(),
        # so we subtract 1 to match Python's list positions (which start at 0).
        if 0 <= index - 1 < len(self.transactions):
            removed = self.transactions.pop(index - 1)
            self.save_transactions()
            print(f"Deleted: {removed}\n")
        else:
            print("Invalid transaction number.\n")

    def save_transactions(self):
        # Convert every Transaction object in the list into a dictionary,
        # because json.dump() cannot save custom objects directly.
        data = [t.to_dict() for t in self.transactions]
        with open(FILE_NAME, "w") as f:
            json.dump(data, f, indent=4)  # indent=4 makes the file readable

    def load_transactions(self):
        # Only try to load if the file actually exists.
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as f:
                data = json.load(f)
                # Convert each dictionary back into a Transaction object.
                self.transactions = [
                    Transaction(d["t_type"], d["category"], d["amount"], d["note"], d["date"])
                    for d in data
                ]


def main():
    # Create one FinanceTracker object. This is the "manager"
    # we will keep using throughout the program.
    tracker = FinanceTracker()

    while True:  # keep showing the menu until the user chooses to exit
        print("===== PERSONAL FINANCE TRACKER =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View All Transactions")
        print("4. View Income Only")
        print("5. View Expenses Only")
        print("6. Show Balance Summary")
        print("7. Delete a Transaction")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter category (e.g. Salary, Bonus): ")
            # float() is used because money can have decimal values (e.g. 99.50)
            amount = float(input("Enter amount: "))
            note = input("Enter note (optional): ")
            tracker.add_transaction("income", category, amount, note)

        elif choice == "2":
            category = input("Enter category (e.g. Food, Rent, Travel): ")
            amount = float(input("Enter amount: "))
            note = input("Enter note (optional): ")
            tracker.add_transaction("expense", category, amount, note)

        elif choice == "3":
            tracker.view_transactions()

        elif choice == "4":
            tracker.view_by_type("income")

        elif choice == "5":
            tracker.view_by_type("expense")

        elif choice == "6":
            tracker.show_summary()

        elif choice == "7":
            tracker.view_transactions()
            try:
                num = int(input("Enter transaction number to delete: "))
                tracker.delete_transaction(num)
            except ValueError:
                print("Please enter a valid number.\n")

        elif choice == "8":
            print("Goodbye! Keep tracking your money wisely.")
            break  # exits the while loop, ending the program

        else:
            print("Invalid choice. Try again.\n")


# This ensures main() only runs when this file is executed directly,
# not when it's imported into another file.
if __name__ == "__main__":
    main()