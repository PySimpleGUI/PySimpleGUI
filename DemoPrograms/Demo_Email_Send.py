import PySimpleGUI as sg

'''
    Copyright 2019 PySimpleGUI.org
    Based on a send-email script originally written by by Israel Dryer
'''

# used for sending the email
import smtplib  as smtp
# used to build the email
from email.message import EmailMessage

# create and send email
def send_an_email(from_address, to_address, subject, message_text, user, password):
    # SMTP Servers for popular free services... add your own if needed. Format is: address, port
    google_smtp_server = 'smtp.gmail.com', 587
    microsoft_smtp_server = 'smtp.office365.com', 587
    yahoo_smtp_server = 'smtp.mail.yahoo.com', 587  # or port 465

    # open the email server connection
    if 'gmail' in user:
        smtp_host, smtp_port = google_smtp_server
    elif 'hotmail' in user or 'live' in user:
        smtp_host, smtp_port = microsoft_smtp_server
    elif 'live' in user:
        smtp_host, smtp_port = microsoft_smtp_server
    elif 'yahoo' in user:
        smtp_host, smtp_port = yahoo_smtp_server
    else:
        sg.popup('Username does not contain a supported email provider')
        return
    server = smtp.SMTP(host=smtp_host, port=smtp_port)
    server.starttls()
    server.login(user=user, password=password)

    # create the email message headers and set the payload
    msg = EmailMessage()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.set_payload(message_text)

    # open the email server and send the message
    server.send_message(msg)

    server.close()

'''
    important notes about using gmail

    - Gmail has locked things down pretty good with what it considers less secure apps. That 
        would include access your Gmail account from the smtplib library in Python. However, there 
        is a work around. You can enable access from "Less Secure Apps" by going to your Gmail 
        account and enabling that feature. However, you should do this at your own peril, and after 
        carefully reading the warnings: https://support.google.com/accounts/answer/6010255.

    smtplib | https://docs.python.org/3/library/smtplib.html?#module-smtplib   
    email.message | https://docs.python.org/3/library/email.message.html?#module-email.message   
    email examples in Python | https://docs.python.org/3.7/library/email.examples.html  
'''

def main():
    sg.change_look_and_feel('Dark Blue 3')
    layout = [[sg.Text('Send an Email', font='Default 18')],
              [sg.T('From:', size=(8,1)), sg.Input(key='-EMAIL FROM-')],
              [sg.T('To:', size=(8,1)), sg.Input(key='-EMAIL TO-')],
              [sg.T('Subject:', size=(8,1)), sg.Input(key='-EMAIL SUBJECT-')],
              [sg.T('Mail login information', font='Default 18')],
              [sg.T('User:', size=(8,1)), sg.Input(key='-USER-')],
              [sg.T('Password:', size=(8,1)), sg.Input(password_char='*', key='-PASSWORD-')],
              [sg.Multiline('Type your message here', size=(60,10), key='-EMAIL TEXT-')],
              [sg.Button('Send'), sg.Button('Exit')]]

    window = sg.Window('Send An Email', layout)

    while True:  # Event Loop
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        if event == 'Send':
            sg.popup_quick_message('Sending your message... this will take a moment...', background_color='red')
            send_an_email(from_address=values['-EMAIL FROM-'],
                          to_address=values['-EMAIL TO-'],
                          subject=values['-EMAIL SUBJECT-'],
                          message_text=values['-EMAIL TEXT-'],
                          user=values['-USER-'],
                          password=values['-PASSWORD-'])

    window.close()

main()