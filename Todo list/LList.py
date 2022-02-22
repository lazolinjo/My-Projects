from asyncio import tasks
from tkinter import *
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import InputText
import pickle

file_object = open ('saved.txt', 'a') 

def focus_control(event):
    if window['todo_item'].get() == '':
        window['todo_item'].update(value=defaultText)
    window['todo_item'].update(select=True)
    # window.refresh()
    return None


defaultText = "Enter your text here"
tasks = []

layout = [
    [sg.Text('ToDo')],
    [sg.InputText('Enter ToDo Item', key='todo_item'), sg.Button(button_text='Add', key="add_save")],
    [sg.Listbox(values=tasks, size=(40, 10), key="items"), sg.Button('Delete'), sg.Button('Edit')],
]

window = sg.indow('LList', layout, icon=r'logo.ico', finalize=True)
window['todo_item'].update(select=True)
window['todo_item'].Widget.bind("<FocusIn>", focus_control)

while True:  # Event Loop
    event, values = window.Read()
    if event == "add_save":
        tasks.append(values['todo_item'])
        window.FindElement('items').Update(values=tasks)
        window.FindElement('add_save').Update("Add")
        window['todo_item'].update('')

    elif event == "Delete":
        tasks.remove(values["items"][0])
        window.FindElement('items').Update(values=tasks)

    elif event == "Edit":
        edit_val = values["items"][0]
        tasks.remove(values["items"][0])
        window.FindElement('items').Update(values=tasks)
        window.FindElement('todo_item').Update(value=edit_val)
        window.FindElement('add_save').Update("Save")

    elif event == None:
        break

file_object.write('tasks')
file_object.close()
window.Close()