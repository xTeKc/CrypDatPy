import PySimpleGUI as sg

#define window contents
layout = [[sg.Text("Enter Contract Address")],
          [sg.Input(key="-INPUT-")],
          [sg.Text(size=(40,1), key="-OUTPUT-")],
          [sg.Button("Search"), sg.Button("End")]
          ]