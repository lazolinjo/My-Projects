import PySimpleGUI as sg

todo = []

layout = [
    [sg.Text('Todo')],
    [sg.InputText('Enter Todo Item', key='todoKey'), sg.Button(button_text='Add', key="add_save")],
    [sg.Listbox(values=todo, size=(40, 10), key="items"), sg.Button('Delete'), sg.Button('Edit')],
]

window = sg.Window('LList', layout, icon=r'C:\Users\Andricka\Desktop\Projects\My-Projects\Todo list\logo.ico')
while True:  # event loop
    event, values = window.Read()
    if event == "add_save":
        todo.append(values['todoKey'])
        window.FindElement('items').Update(values=todo)
        window.FindElement('add_save').Update("Add")
    elif event == "Delete":
        todo.remove(values["items"][0])
        window.FindElement('items').Update(values=todo)
    elif event == "Edit":
        edit_val = values["items"][0]
        todo.remove(values["items"][0])
        window.FindElement('items').Update(values=todo)
        window.FindElement('todoKey').Update(values=edit_val)
        window.FindElement('add_save').Update("Save")
    elif event == None:
        break

window.Close()
