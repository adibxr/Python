def todo_list():
    tasks = []

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter a new task: ")
            tasks.append(task)
            print("Task added successfully!")
        elif choice == '2':
            print("\nYour Tasks:")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
        elif choice == '3':
            try:
                task_number = int(input("Enter task number to delete: "))
                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"Removed task: {removed_task}")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")
        elif choice == '4':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

todo_list()
