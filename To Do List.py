import os

def get_path(name, filepath):
    if os.path.exists(filepath):
        return os.path.join(filepath, f"{name}.txt")
    elif filepath == "":
        return f"{name}.txt"
    else:
        os.makedirs(filepath)
        return os.path.join(filepath, f"{name}.txt")

def create_file():
    name = input("Enter the name of the file (without extension): ")
    filepath = input("Enter the directory path where you want to save the file (leave blank for current directory): ")
    full_path = get_path(name, filepath)
    with open(f"{full_path}", "w", encoding="utf-8") as file:
        pass
    print("File created successfully.\n")

def show_task():
    name = input("Enter the name of the file (without extension): ")
    filepath = input("Enter the directory path where the file is located (leave blank for current directory): ")
    full_path = get_path(name, filepath)
    display_tasks(full_path)
    return full_path

def display_tasks(full_path):
    with open(f"{full_path}", "r", encoding="utf-8") as file:
        tasks = file.readlines()
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task.strip()}")
        print()
    else:
        print("No tasks found.\n")

def add_task():
    name = input("Enter the name of the file (without extension): ")
    filepath = input("Enter the directory path where the file is located (leave blank for current directory): ")
    full_path = get_path(name, filepath)
    total_tasks = int(input("Enter the number of tasks you want to add (number only): "))
    with open(f"{full_path}", "a", encoding="utf-8") as file:
        for i in range(total_tasks):
            task = input(f"Enter task {i + 1}: ")
            file.write(f"{task} [ ]\n")
    print("Tasks added successfully.\n")

def update_task():
    full_path = show_task()
    task_number = int(input("Enter the task number to mark as completed (number only): "))
    with open(f"{full_path}", "r", encoding="utf-8") as file:
        tasks = file.readlines()
    
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1] = tasks[task_number - 1].replace("[ ]", "[\u2713]")
        with open(f"{full_path}", "w", encoding="utf-8") as file:
            file.writelines(tasks)
        print("Task marked as completed.\n")
    else:
        print("Input Invalid\n")


while True:
    print("=========================================")
    print("Welcome to the To Do List Program")
    print("1. Create To Do List")
    print("2. Add Tasks")
    print("3. Show Tasks")
    print("4. Update Task")
    print("5. Exit")
    print("=========================================")
    choice = int(input("Enter your choice: "))
    print()


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
        print("Invalid choice. Please try again.\n")
        