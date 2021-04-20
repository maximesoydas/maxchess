import PySimpleGUI as sg

layout = [[sg.Text('Enter something'), sg.Input(key='-IN-')],
          [sg.Text('Our Output will go here', key='-OUT-')],
          [sg.Button('Ok'), sg.Button('Exit')]         ]

window = sg.Window('Title', layout)

while True:
    event, values = window.read()
    if event is None or event == 'Exit':
        break
    window['-OUT-'].update(values['-IN-'])
window.close()