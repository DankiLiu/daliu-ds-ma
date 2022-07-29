import PySimpleGUI as sg

# Define the layout of command input area
command_input = [[sg.Text("This is a GUI the robot task-oriented dialog system.")],
                 [sg.Text("Please input your command below")],
                 [sg.InputText(default_text="Put that milk into the fridge."),
                  sg.Button("OK")]]
# Define the layout of the model output
model_output = [[sg.Text("Action"), sg.InputText("Output action from model", key="-ACTION-")],
                [sg.Text("Objects"), sg.InputText("Object names", key="-OBJECTS-")]]
layout = [[sg.Column(command_input), sg.VSeparator(), sg.Column(model_output)]]
# Create the window
window = sg.Window(title="Dialog GUI", layout=layout)

# Create an event loop
while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
