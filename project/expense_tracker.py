print("------ Expense Tracker ------")

FILE_NAME = "expense.txt"

def add_expense():
    item = input("enter item Name : ")
    amount = float(input("Enter Amount : "))


    with open(FILE_NAME , 'a') as file:
        file.write(f"{item} - {amount}\n")

    print("Expense Added!\n")

def view_expense():
    print("\n------ All Expenses ------")
    try:
        with open(FILE_NAME , 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found!")
    print("---------------------------\n")

def Total_expense():
    total = 0
    try:
        with open(FILE_NAME , 'r') as file:
            for line in file:
                parts = line.strip ().split(" - ")
                if len(parts) == 2:
                    amount = float(parts[1])
                    total += amount
    except FileNotFoundError:
        print("File not Found!! ")
    print(f"\nTotal Expense : Rs {total}")

while True:
    print("""
1. Add Expense 
2. View Expense
3. Total Expense 
4. Exit """)
    
    choice = input("Enter Your choice : ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expense()
    elif choice == "3":
        Total_expense()
    elif choice == "4":
        print("Thank You !")
        break
    else:
        print("Somethings Went Wrong Pls try again!!")