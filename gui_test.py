import PySimpleGUI as sg

sg.theme("DarkBlue3")
sg.set_options(font=("Courier New", 11))

width = 80
layout =[
    [sg.Text(" Latest News ", background_color='#000040', text_color='white', font=("Courier New", 11, 'bold')),
     sg.Text("", size=(width, 1), background_color='#000080', text_color='white', key='news_ticker')],
    [sg.Multiline("", size=(width, 15), expand_x=True, key='news')],
    [sg.Button("Update")],
]
window = sg.Window("Title", layout, resizable=True, finalize=True)
text = ' '*width
while True:

    event, values = window.read(timeout=200)

    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Update':
        text = ('     '.join(map(str.strip, values['news'].split('\n')))).ljust(width)

    window['news_ticker'].update(value=text)
    text = text[1:] + text[0]

window.close()