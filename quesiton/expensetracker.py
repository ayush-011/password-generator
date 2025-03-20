expenseTracker = {}

print("\nFeatures of Expense Tracker")
print("1. Add a new expense amount, category, and description")
print("2. View all expenses")
print("3. View total expenses")
print("4. Delete an expense")
print("5. Exit")

print("Please select the operation 1/5:")
choice = int(input("Enter:"))

if choice == 1:
    print("You choose option 1")
    print("Enter the expense you want to enter")
    task_id = len