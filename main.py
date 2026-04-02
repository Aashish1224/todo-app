#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d,%Y %H:%M:%S")
print("it is", now)
while True:
    # get user input and strip space chars from it
    user_action = input("type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

# check if user action is add

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

#Show function

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate (todos):
            item = item.strip('\n')
            row = f"{index + 1}- {item}"
            print(row)

#Edit function

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("your command is not valid")
            continue

#Complete function

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list "
            print(message)
        except ValueError:
            print("There is no item with that number")
            continue

#Exit function

    elif user_action.startswith('exit'):
        break
    else:
        print("command is not valid")


print("Goodbye!")


