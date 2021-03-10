import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import InputText

def focus_control(event):
    if window['inputKey'].get() == '':
        window['inputKey'].update(value=defaultText)
    window['inputKey'].update(select=True)
    # window.refresh()
    return None

defaultText = "Enter your text here"
todo = []

layout = [
    [sg.Text('Todo')],
    [sg.InputText(defaultText, key='inputKey' ), sg.Button(button_text='Add', key="addKey")],
    [sg.Listbox(values=todo, size=(40, 10), key="itemKey"), sg.Button('Delete'),sg.Button('Edit')],
]

window = sg.Window('LList', layout, icon=r'C:\Users\Andricka\Desktop\Projects\My-Projects\Todo list\logo.ico', finalize=True)
window['inputKey'].Widget.bind("<FocusIn>", focus_control)
window['inputKey'].update(select=True)

while True:  # event loop
    event, values = window.Read()
    print(event, values)
    if event == None:
        break

    elif event == "Add":
        window['Listbox'].update(value=values['inputKey'])
        window.FindElement('inputKey').Update('')

    if event == "addKey":
        todo.append(values['inputKey'])
        window.FindElement('itemKey').Update(values=todo)

    elif event == "Delete":
        todo.remove(values["itemKey"][0])
        window.FindElement('itemKey').Update(values=todo)

    elif event == "Edit":
        edit_val = values["itemKey"][0]
        todo.remove(values["itemKey"][0])
        window.FindElement('itemKey').Update(values=todo)
        window.FindElement('inputKey').Update(values=edit_val)
        window.FindElement('addKey').Update("Save")
        
    elif event == None:
        break

window.Close()
