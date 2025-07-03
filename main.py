

tasks = []

while True:
    print("\nMenu:")
    print("(1) Add Task")
    print("(2) View Tasks")
    print("(3) Remove Task")
    print("(4) Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
    elif choice == '2':
        print("\nTasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}: {task}")
    elif choice == '3':
        task = input("Enter task number to remove: ")
        task = int(task)
        if task < 1 or task > len(tasks):
            print("Invalid task number.")
        else:
            tasks.pop(task - 1)

    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")  
    