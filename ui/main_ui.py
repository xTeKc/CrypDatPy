import PySimpleGUI as sg

#define window contents
layout = [[sg.Text("Enter Contract Address")],
          [sg.Input(key="-INPUT-")],
          [sg.Text(size=(40,1), key="-OUTPUT-")],
          [sg.Button("Search"), sg.Button("End")]]

#create window
window = sg.Window("CrypDat", layout)

#display window and interact with it
while True:
    event, values = window.read()
    #check if window session ended
    if event == sg.WINDOW_CLOSED or event == "End":
        break
    