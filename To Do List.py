import os

def create_file():
    name = input("Enter the name of the To Do List file (without extension): ")
    filepath = input("Enter the directory path where you want to save the file (leave blank for current directory): ")
    if os.path.exists(filepath):
        full_path = os.path.join(filepath, f"{name}.txt")
    else:
        os.makedirs(filepath)
        full_path = os.path.join(filepath, f"{name}.txt")
    with open(f"{full_path}.txt", "w", encoding="utf-8") as file:
        pass
    print("To Do List file created successfully.\n")

def add_task():
    name = input("Enter the name of the To Do List file (without extension): ")
    total_tasks = int(input("Enter the number of tasks you want to add: "))
    with open(f"{name}.txt", "a", encoding="utf-8") as file:
        for i in range(total_tasks):
            task = input(f"Enter task {i + 1}: ")
            file.write(f"{task} [ ]\n")

def show_task():
    name = input("Enter the name of the To Do List file (without extension): ")
    with open(f"{name}.txt", "r", encoding="utf-8") as file:
        tasks = file.readlines()
    print("Current Tasks:")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task.strip()}")

def update_task():
    name = input("Enter the name of the To Do List file (without extension): ")
    show_task()
    task_number = int(input("Enter the task number to mark as completed: "))
    with open(f"{name}.txt", "r", encoding="utf-8") as file:
        tasks = file.readlines()
    
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1] = tasks[task_number - 1].replace("[ ]", "[\u2713]")
        with open(f"{name}.txt", "w", encoding="utf-8") as file:
            file.writelines(tasks)
        print("Task marked as completed.\n")
    else:
        print("Input Invalid")

def list_files():
while True:
    print("=========================================")
    print("Welcome to the To Do List Program")
    print("1. Create To Do List")
    print("2. Add Tasks")
    print("3. Show Tasks")
    print("4. Update Task")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_file()
    elif choice == 2:
        add_task()
    elif choice == 3:
        show_task()
    elif choice == 4:
        update_task()
    elif choice == 5:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
        