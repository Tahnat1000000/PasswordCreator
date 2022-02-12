import PySimpleGUI as sg, numpy, random

def main():
    sg.theme('DarkAmber')
    layo = [[sg.Text("Welcome to password creator", justification="center")],
            [sg.Text("Enter lenght of password(1-20):")],
            [sg.Input(key="-length-", justification="center")],
            [sg.Text("Password include:")],
            [sg.Checkbox("ABC", key="0")],
            [sg.Checkbox("abc", key="1")],
            [sg.Checkbox("123", key="2")],
            [sg.Checkbox("!@#", key="3")],
            [sg.Button(button_text="CREATE NEW PASSWORD", key="-CREATE-")],
            [sg.Input("NEW PASSWORD", justification="center", key="-output-")]]

    win = sg.Window("Password Creator", layout=layo, size=(300, 300), element_justification="center")

    charType = numpy.array(["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz", "0123456789", "!@#$%^&*()"])

    while True:
        event, values = win.read()
        passwordChars = ""
        if values['0'] == True:
            passwordChars = passwordChars.__add__(charType[0])
        if values['1'] == True:
            passwordChars = passwordChars.__add__(charType[1])
        if values['2'] == True:
            passwordChars = passwordChars.__add__(charType[2])
        if values['3'] == True:
            passwordChars = passwordChars.__add__(charType[3])
        if event == "-CREATE-":
            pass_len = len(str(values['-length-']))
            if (values['0'] == True or values['1'] == True or values['2'] == True or values[
                '3'] == True) and pass_len >= 1 and pass_len <= 2:
                new_password = ""
                if str(values["-length-"]).isdecimal() and int(values["-length-"]) <= 20:
                    for i in range(int(values["-length-"])):
                        new_password += random.choice(passwordChars)
                win.Element("-output-").update(new_password)
        if event == sg.WIN_CLOSED:
            break

    win.close()

if __name__ == '__main__':
    main()
