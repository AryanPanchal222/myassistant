items = []
prices = []

while True:
    print("1. Add Item")
    print("2. View Bill")
    print("3. Exit")
    
    choice = input("Enter choice : ")

    if choice == "1":
        name = input("Enter Item  name : ")
        Price = float(input(f"Enter {name}  Price : "))
        items.append(name)
        prices.append(Price)
        print("Item Added")

    elif choice == "2":
        print("---- Youe bill ----")
        total = 0
        for i in range (len(items)):
            print(f"{items[i]} : Rs {prices[i]}")
            total +=prices[i]

        print("------------------------")
        print(f"Total Amount: Rs {total}")
        print ("------------------------\n")
        
    elif choice == "3":
        prices("Thank you for buying")
        break
    else:
        print("Invalid Choice Pls Try Again!!!")