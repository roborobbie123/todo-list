print("TODO LIST")
todo_list = []

while True:
    user_input = input("Type add, show, edit, delete, or exit: \n")
    match user_input.strip():
        case 'add' | 'insert':
            todo = input("Enter a todo: ")
            todo_list.append(todo)
            print(f"Added {todo.upper()} to todo list")

        case 'show' | 'display':
            if len(todo_list) == 0:
                print("Todo list is empty")
                continue
            else:
                print("TODO List:")
                for i in range(len(todo_list)):
                    print(f"{i + 1}) {todo_list[i].title()}")

        case 'edit':
            if len(todo_list) == 0:
                print("Todo list is empty")
                continue
            for i in range(len(todo_list)):
                print("TODO List:")
                print(f"{i + 1}) {todo_list[i].title()}")
            index = int(input("Enter an item number to edit: "))
            if index > len(todo_list):
                print("Invalid item")
                continue
            edit = input("Enter updated value: ")
            todo_list[index - 1] = edit
            for i in range(len(todo_list)):
                print("TODO List:")
                print(f"{i + 1}) {todo_list[i].title()}")

        case 'delete':
            if len(todo_list) == 0:
                print("Todo list is empty")
                continue
            for i in range(len(todo_list)):
                print("TODO List:")
                print(f"{i + 1}) {todo_list[i].title()}")
            index = int(input("Enter an item number to delete: "))
            if index > len(todo_list):
                print("Invalid item")
                continue
            print(f"Deleting {todo_list[index - 1]}...")
            todo_list.remove(todo_list[index - 1])

        case 'exit' | 'leave':
            print("Exiting...")
            break

        case default:
            print("Please enter a valid input")
