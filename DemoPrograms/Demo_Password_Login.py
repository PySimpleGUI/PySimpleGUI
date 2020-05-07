#!/usr/bin/env python
import PySimpleGUI as sg
import hashlib

"""
    Create a secure login for your scripts without having to include your password 
    in the program.  Create an SHA1 hash code for your password using the GUI. Paste into variable in final program
    1. Choose a password
    2. Generate a hash code for your chosen password by running program and entering 'gui' as the password
    3. Type password into the GUI
    4. Copy and paste hash code from GUI into variable named login_password_hash
    5. Run program again and test your login!
    6. Are you paying attention? The first person that can post an issue on GitHub with the
       matching password to the hash code in this example gets a $5 PayPal payment
"""


def main():
    # Use this GUI to get your password's hash code
    def HashGeneratorGUI():
        layout = [
            [sg.Text('Password Hash Generator', size=(30, 1), font='Any 15')],
            [sg.Text('Password'), sg.Input(key='-password-')],
            [sg.Text('SHA Hash'), sg.Input('', size=(40, 1), key='hash')],
        ]

        window = sg.Window('SHA Generator', layout,
                           auto_size_text=False,
                           default_element_size=(10, 1),
                           text_justification='r',
                           return_keyboard_events=True,
                           grab_anywhere=False)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break

            password = values['-password-']
            try:
                password_utf = password.encode('utf-8')
                sha1hash = hashlib.sha1()
                sha1hash.update(password_utf)
                password_hash = sha1hash.hexdigest()
                window['hash'].update(password_hash)
            except:
                pass
        window.close()

    # ----------------------------- Paste this code into your program / script -----------------------------
    # determine if a password matches the secret password by comparing SHA1 hash codes
    def PasswordMatches(password, a_hash):
        password_utf = password.encode('utf-8')
        sha1hash = hashlib.sha1()
        sha1hash.update(password_utf)
        password_hash = sha1hash.hexdigest()
        return password_hash == a_hash

    login_password_hash = '6adfb183a4a2c94a2f92dab5ade762a47889a5a1'  # helloworld
    password = sg.popup_get_text(
        'Password: (type gui for other window)', password_char='*')
    if password == 'gui':                  # Remove when pasting into your program
        HashGeneratorGUI()                              # Remove when pasting into your program
        return                                          # Remove when pasting into your program
    if password and PasswordMatches(password, login_password_hash):
        print('Login SUCCESSFUL')
    else:
        print('Login FAILED!!')


if __name__ == '__main__':
    sg.theme('DarkAmber')
    main()
