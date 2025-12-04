books = []
prices = []


while True:

    print("1. Add book")
    print("2. view bill")
    print("3. Exit")

    choice = (input("Enter YOur choice : "))

    if choice == "1":
        print("----Book add to Cart ----")
        name = input("Enter Book name : ")
        price = float(input("Enter book price : "))
        books.append(name)
        prices.append(price)
        print("Book added into cart.")
    
    elif choice == "2":
        print ("---- Your Bill ----")
        Total = 0
        for i in range(len(books)):
            print(f"{books[i]} : Rs {prices[i]}")
            Total += prices[i]
        print("------------------------")
        print(f"Total Bill is : {Total}")
        print("------------------------")
    
    elif choice == "3":
        print("Thank you for visit! ")
        break

    else:
        print("Somethings went wrong pls try again!!!")