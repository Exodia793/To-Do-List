def create_file():
    with open("To Do List.txt", "w") as file:
        file.write("To Do List:\n")
    print("To Do List file created successfully.\n")


while True:
    print("=========================================")
    print("Welcome to the To Do List Program")
    print("1. Create To Do List")
    print("2. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_file()
    elif choice == 2:
        break
    else:
        print("Invalid choice. Please try again.")
        