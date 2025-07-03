

tasks = []

try:
    with open("tasks.txt", "r") as f:
        tasks = f.read().splitlines()
except FileNotFoundError:
    pass

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
        for i, task in enumerate(tasks): # ["task1", "task2", "task3"] -> [(0, "task1"), (1, "task2"), (2, "task3")]
            print(f"{i + 1}: {task}")
    elif choice == '3':
        task = input("Enter task number to remove: ")
        try:
            task = int(task)
            if task < 1 or task > len(tasks):
                print("Invalid task number.")
            else:
                tasks.pop(task - 1)
        except ValueError:
            print("Invalid task number.")
    elif choice == '4':
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(f"{task}\n")
        break
    else:
        print("Invalid choice. Please try again.")  
    