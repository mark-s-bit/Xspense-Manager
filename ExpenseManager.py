import sqlite3
from datetime import datetime

# Connect to the SQLite database
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()

# Insert into 'users' table
def insert_user(username, email):
    cursor.execute('''
        INSERT INTO users (username, email)
        VALUES (?, ?)
    ''', (username, email))
    conn.commit()
    print(f"User '{username}' added successfully!")

# Insert into 'categories' table
def insert_category(category_name):
    cursor.execute('''
        INSERT INTO categories (name)
        VALUES (?)
    ''', (category_name,))
    conn.commit()
    print(f"Category '{category_name}' added successfully!")

# Insert into 'income' table
def insert_income(user_id, amount, source, date):
    cursor.execute('''
        INSERT INTO income (user_id, amount, source, date)
        VALUES (?, ?, ?, ?)
    ''', (user_id, amount, source, date))
    conn.commit()
    print(f"Income of {amount} added for user_id {user_id}.")

# Insert into 'budget' table
def insert_budget(user_id, category_id, amount, start_date, end_date):
    cursor.execute('''
        INSERT INTO budget (user_id, category_id, amount, start_date, end_date)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, category_id, amount, start_date, end_date))
    conn.commit()
    print(f"Budget of {amount} added for user_id {user_id} in category {category_id}.")

# Insert into 'expenses' table
def insert_expense(user_id, category_id, amount, description, date):
    cursor.execute('''
        INSERT INTO expenses (user_id, category_id, amount, description, date)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, category_id, amount, description, date))
    conn.commit()
    print(f"Expense of {amount} added for user_id {user_id} in category {category_id}.")

# Get user input for inserting data
def get_user_input():
    while True:
        print("\nWhat would you like to do?")
        print("1. Add Income")
        print("2. Add Budget")
        print("3. Add Category")
        print("4. Add Expense")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            user_id = int(input("Enter User ID: "))
            amount = float(input("Enter income amount: "))
            source = input("Enter income source: ")
            date = input("Enter date (YYYY-MM-DD): ")
            insert_income(user_id, amount, source, date)

        elif choice == "2":
            user_id = int(input("Enter User ID: "))
            category_id = int(input("Enter Category ID: "))
            amount = float(input("Enter budget amount: "))
            start_date = input("Enter budget start date (YYYY-MM-DD): ")
            end_date = input("Enter budget end date (YYYY-MM-DD): ")
            insert_budget(user_id, category_id, amount, start_date, end_date)

        elif choice == "3":
            category_name = input("Enter category name: ")
            insert_category(category_name)

        elif choice == "4":
            user_id = int(input("Enter User ID: "))
            category_id = int(input("Enter Category ID: "))
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            date = input("Enter date (YYYY-MM-DD): ")
            insert_expense(user_id, category_id, amount, description, date)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

# Start the program
if __name__ == "__main__":
    print("Welcome to the Expense Manager!")
    get_user_input()

# Close the database connection when done
conn.close()
