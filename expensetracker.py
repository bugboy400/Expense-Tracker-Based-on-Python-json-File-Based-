import json
import os
from datetime import datetime

def home():
    print("1.Add Expense")
    print("2.View Expense")
    print("3.Search Expense")
    print("4.Delete Expense")
    print("5.Exit")
    choice=int(input("Enter your choice(1-6):"))
    if choice<0 or choice>5:
        print(" Invalid Option. PLEASE CHOOSE CORRECT OPTION")
        home()
        return
    elif choice==1:
        add_expense()
        
    elif choice==2:
        view_expense()
        runagain()
       
    elif choice==3:
        search_expense()
        runagain()
    elif choice==4:
        delete_expense()
    else:
        print("👋 Exiting the Expense Tracker. Goodbye!")
        exit()
        
def add_expense():
    print("Enter the Expense Information")
    item = input("Enter the Expense Item Name: ")
    price = float(input("Enter the Expense Item Price: "))
    date = datetime.now().strftime("%Y-%m-%d")
    
    expense = {"item": item, "price": price, "date": date}
    
    # Load existing expenses
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as f:
            try:
                expenses = json.load(f)
                # Ensure expenses is a list
                if not isinstance(expenses, list):
                    expenses = []
            except json.JSONDecodeError:
                expenses = []
    else:
        expenses = []
    
    # Add new expense
    expenses.append(expense)
    
    # Save updated list
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=4)
    
    print("✅"+ item+ " added successfully!")
    runagain()

    
# def view_expense():
#     print("\nEXPENSE LIST")
#     print("--------------------------------------------------")
#     print("S.No | Item Name        | Price   | Date")
#     print("--------------------------------------------------")

#     with open("expenses.json", "r") as f:
#         data = json.load(f)

#         for i, expense in enumerate(data, start=1):
#             print(f"{i:<4} | {expense['item']:<15} | {expense['price']:<7} | {expense['date']}")

#     print("--------------------------------------------------")
#     print(f"Total Items: {len(data)}")
#     return data

def view_expense():
    print("\nEXPENSE LIST")
    print("--------------------------------------------------")
    print("S.No | Item Name        | Price   | Date")
    print("--------------------------------------------------")

    # Check if file exists
    if not os.path.exists("expenses.json"):
        print("No expenses found. File does not exist.")
        return []

    try:
        with open("expenses.json", "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("⚠️ Error: expenses.json is not a valid JSON file.")
        return []
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
        return []

    if not data:
        print("No expenses found.")
        print("--------------------------------------------------")
        return []

    for i, expense in enumerate(data, start=1):
        print(f"{i:<4} | {expense['item']:<15} | {expense['price']:<7} | {expense['date']}")

    print("--------------------------------------------------")
    print(f"Total Items: {len(data)}")

    return data  # ✅ So delete_expense() can use it

    

    
def search_expense():
    print("Search Expense")
    print("1.Search by Item Name\n2.Search by Date")
    choiceto=int(input("Enter your choice(1 or 2):"))
    if os.path.exists("expenses.json"):
        if choiceto==1:
            searchbyname()
        else:
         searchbydate()
    else:
        print("No expenses found")
    runagain()
    
def searchbyname():
    searchhere = input("Enter the Item Name to Search: ")
    with open("expenses.json", "r") as f:
        items = json.load(f)
        found = False
        count = 1
        for item in items:
            if searchhere.lower() == item['item'].lower():
                if not found:  # print header only once
                    print("\nITEM/S FOUND WITH THE NAME '" + searchhere + "' !!!")
                    print("--------------------------------------------------")
                    print("S.No | Item Name        | Price   | Date")
                    print("--------------------------------------------------")
                print(f"{count:<4} | {item['item']:<15} | {item['price']:<7} | {item['date']}")
                count += 1
                found = True
        if not found:
            print("Item not found with the name " + searchhere + " provided")

               
def searchbydate():
    print("Search by Date")
    datesearch = input("Enter the Date to Search(YYYY-MM-DD): ")
    with open("expenses.json", "r") as f:
        expenses = json.load(f)

        found = False
        count = 1  # serial number
        for expense in expenses:
            if datesearch == expense['date']:
                if not found:  # print header only once
                    print("\nITEM/S FOUND FOR THE GIVEN " + datesearch + " DATE!!!")
                    print("--------------------------------------------------")
                    print("S.No | Item Name        | Price   | Date")
                    print("--------------------------------------------------")
                print(f"{count:<4} | {expense['item']:<15} | {expense['price']:<7} | {expense['date']}")
                count += 1
                found = True

        if not found:
            print("No items found on the date " + datesearch + " provided")
         
def delete_expense():
    data = view_expense()
    if not data:
        return  # No expenses to delete

    try:
        todelete = int(input("Enter the Expense Number to delete: "))
        if 1 <= todelete <= len(data):
            deleteditem = data.pop(todelete - 1)
            with open("expenses.json", "w") as f:
                json.dump(data, f, indent=4)
            print(f"✅ {deleteditem['item']} Deleted Successfully!")
        else:
            print("❌ Invalid number. Please enter a number from the list.")
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")

    runagain()


    
    
def runagain():
    againchoice=input("Do you want to continue? (y/n): ").lower()
    if againchoice=='y':
        home()
    else:
        print("👋 Exiting the Expense Tracker. Goodbye!")
        exit()
        
home()