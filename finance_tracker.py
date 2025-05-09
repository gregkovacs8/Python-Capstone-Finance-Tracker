# Personal Finance Tracker

print("Welcome to the Personal Finance Tracker!")
expenses = {}

#All functions needed

#Function to add expense
def add_expense(data):
    try:
        description = input("Enter expense description: ").strip()
        if not description:
            print("Description cannot be empty")
            return

        category = input("Enter category: ").strip()
        if not category:
            print("Category cannot be empty")
            return

        amount_input = input("Enter amount: ").strip()
        amount = float(amount_input)

        if amount < 0:
            print("Amount cannot be negative.")
            return

        if category not in data:
            data[category] = [] 
        data[category].append((description, amount)) 
        
        print("Expense added successfully.")
   
    except ValueError:
        print("Invalid amount. Please enter a number.")

#Function to view expenses
def view_expenses(data):
    if not data:
        print("No expenses recorded yet.")
        return
    
    for category, expense_list in data.items():
        print(f"\nCategory: {category}")
        for description, amount in expense_list:
            print(f"  - {description}: ${amount:.2f}")

#Function to view summary
def view_summary(data):
    if not data:
        print("No expenses recorded yet.")
        return
    
    print("\nSummary:")
    for category, expense_list in data.items():
        total = sum(amount for _, amount in expense_list)
        print(f"{category}: ${total:.2f}")


#Menu loop
while True:
    print("What would you like to do?")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense(expenses)
        print("========================================")
    elif choice == "2":
        view_expenses(expenses)
        print("========================================")
    elif choice == "3":
        view_summary(expenses)
        print("========================================")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")

