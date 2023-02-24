import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_input = input("Type add, show, edit, complete or exit: ").strip()

    if user_input.startswith('add') or user_input.startswith('new'):
        todo = user_input[4:] + '\n'
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)
    elif user_input.startswith("show"):
        todos = functions.get_todos()
        for i, todo in enumerate(todos):
            todo = todo.strip('\n')
            print(f"{i + 1}-{todo}")
            i += 1

    elif user_input.startswith("edit"):
        try:
            number = int(user_input[5:])
            number = number - 1
            new_todo = input("Enter a new todo: ") + '\n'
            todos = functions.get_todos()
            todos[number] = new_todo
            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid")

    elif user_input.startswith('complete'):
        try:
            number = int(user_input[9:])
            number = number - 1
            todos = functions.get_todos()
            todos.pop(number)
            functions.write_todos(todos)
        except IndexError:
            print("There is no item with that number")
        except ValueError:
            print("Your command is not valid")

    elif "exit" in user_input:
        break

    else:
        print("try again")
