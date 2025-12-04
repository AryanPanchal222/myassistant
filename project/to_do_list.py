import os

FILE_NAME = "task.txt"

def load_tasks():
    tasks =  []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME , 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(" | ")
                if len(parts) == 2:
                    title , status = parts
                    tasks.append({"title" : title , "status : ": status})

    return tasks
def save_tasks(tasks):
    with open (FILE_NAME , "w") as file:
        for t in tasks:
            file.write(f"{t['title']} | {t['status']}\n")

def add_taks(tasks):
    title = input("Enter your task title : ")
    tasks.append({"title" : title , "status" : "Panding"}) 
    print("Task added1\n")

def view_task(tasks):
    if not tasks:
        print("No tasks found \n")
        return
    print("--- Your Tasks ---")
    for i , t in enumerate(tasks , start=1):
        print(f"{i}.{t['title']} = {t['status']}")
    print("------------------")
def mark_down(tasks):
    view_task(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number  to marks as Done : "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["status"] = "Done"
            print("Task markdown as Done!\n")
        else:
            print("Invalid Task number!!\n")
    except ValueError:
        print("Enter valid number!!! ")

def delete_task(tasks):
    view_task(tasks)
    if not tasks:
        return
    
    try:
         num = int(input("Enter number which task you want to delete : "))
         if 1<= num <= len(tasks):
             removed = tasks.pop(num-1)
             print(f"Deleted : {removed['title']}\n")
         else:
            print("Invalid Task number!!\n")
    except ValueError:
        print("Enter valid number!!! ")

def main():
    print("------ To_Do_List -----")
    
    tasks = load_tasks()

    while True:
        print("""
1. Add Task
2. View Tasks
3. Mark Task as Done
4. Delete Task
5. Exit
""")
        choice = input("enter your choice  : ")
        if choice == "1":
            add_taks(tasks)
            save_tasks(tasks)
        elif choice == "2":
            view_task(tasks)
        elif choice == "3":
            mark_down(tasks)
            save_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again!\n")
if __name__ == "__main__":
    main()