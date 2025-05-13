#  To-Do List App (Text-Based)
# Let the user add, view, and delete tasks from a simple list using menu options.




# if choice == "1":
#     task = input("What you up to?")
#     tasks.append(task)
# if choice == "2":
#     for task in tasks:
#         print("-" + tasks)
# if choice == "4":
#     print("good BYE")

# else:
#     print("invalid")

tasks = []

while True:
    print("--- TO-DO LIST ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)

    elif choice == "2":
        print("Your tasks:")
        if not tasks:
            print("No tasks yet.")
        else:
            i = 1
            for task in tasks:
                print(str(i) + ". " + task)
                i += 1

    elif choice == "3":
        if not tasks:
            print("\nNo tasks to remove.")
        else:
            print("Your tasks:")
            i = 1
            for task in tasks:
                print(str(i) + ". " + task)
                i += 1

            task_number = input("Enter the task number to remove: ")

            if task_number.isdigit():
                task_number = int(task_number)
                if 1 <= task_number <= len(tasks):
                    removed = tasks.pop(task_number - 1)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
