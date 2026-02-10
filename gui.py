import functions
import FreeSimpleGUI as Sg

from functions import write_todos

label =Sg.Text("Type in a To-Do")
input_box = Sg.InputText(tooltip = "Enter todo",key="todo")
add_button =  Sg.Button("Add")
list_box = Sg.Listbox(functions.get_todos(),key="todos",
                      enable_events=True,
                      size=(45,10))
edit_button = Sg.Button("Edit")
complete_button = Sg.Button("Complete")
exit_button = Sg.Button("Exit",key="Exit")


window = Sg.Window("My To-Do App",
                   layout= [[label],[input_box,add_button],[list_box,edit_button,complete_button],[exit_button]],
                   font=("Helvetica",20))

while True:
    event,values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            edit_todo = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index =  todos.index(edit_todo)
            todos[index] = new_todo + '\n'
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Complete":
            todo_complete = values['todos'][0]
            print(todo_complete)
            todos = functions.get_todos()
            todos.remove(todo_complete)
            functions,write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(values="")
        case "Exit":
            break
        case Sg.WIN_CLOSED:
            break


window.close()