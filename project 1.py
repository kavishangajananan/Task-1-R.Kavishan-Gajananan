# To-Do List Program

tasks = []

while True:
    print("========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    # ADD TASK
    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print(" Task added successfully!")

    # VIEW TASKS
    elif choice == "2":
        if len(tasks) == 0:
            print("️ No tasks available.")
        else:
            print(" Your Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    # DELETE TASK
    elif choice == "3":
        if len(tasks) == 0:
            print(" No tasks to delete.")
        else:
            print("Select task number to delete:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            try:
                num = int(input("Enter task number: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print("️ Task '{removed}' deleted successfully!")
                else:
                    print(" Invalid task number.")
            except:
                print(" Please enter a valid number.")

    # EXIT PROGRAM
    elif choice == "4":
        print(" Exiting program... Goodbye!")
        break

    # INVALID INPUT
    else:
        print(" Invalid choice. Please try again.")
