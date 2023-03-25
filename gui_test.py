# hello_psg.py

import PySimpleGUI as sg

layout = [[sg.Text("MUSIC PLAYING:")], [sg.Button("Play")], [sg.Button("Pause")], [sg.Button("Stop")]]

# Create the window
window = sg.Window("Pedro YT Player", layout, margins=(100, 50))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
