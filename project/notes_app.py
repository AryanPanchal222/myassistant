# note app


FILE_NAME = "notes.txt"


while True:
    print("1. Add Note")
    print("2. View Note")
    print("3. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        note = input("Write Your note : "   )
        with open(FILE_NAME , 'a') as file:
            file.write(note + "\n")
    
    elif choice == "2":
        print("---- Your note ----")
        
        try:
            with  open(FILE_NAME , 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print("Notes not Found ")

        print("------------------------\n")

    elif choice == "3":
        print("Good bye !")
        break

    else:
        print("Enter Valid choice")
        