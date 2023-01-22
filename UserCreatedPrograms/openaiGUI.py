import logging
import PySimpleGUI as sg
import openai
import os
import sys
import requests
import urllib.request
from PIL import Image
from io import BytesIO

"""
pip install PySimpleGUI==4.60.4
pip install openai==0.16.0
pip install Pillow==9.2.0
"""
# @https://beta.openai.com/docs/engines/gpt-3

#Get yours at --> https://beta.openai.com/account/api-keys
key = openai.api_key = "yourkey"
logger = logging.getLogger()
logging.basicConfig(filename='answers.txt', level=logging.INFO)

# Defines the modules() and openAi() functions which are used to select the engine, tokens and picture size and generate a response.
def modules(engines):
    model = None
    if engines == "text-davinci-003":
        model = "text-davinci-003"
    elif engines == "text-davinci-002":
        model = "text-davinci-002"
    elif engines == "text-curie-001":
        model = "text-curie-001"
    elif engines == "text-babbage-001":
        model = "text-babbage-001"
    elif engines == "text-ada-001":
        model = "text-ada-001"
    return model

def select_max_tokens(max_tokens):
    token = None
    if max_tokens == 256:
        token = 256
    elif max_tokens == 2000:
        token = 2000
    elif max_tokens == 8000:
        token = 8000
    return token

def picture_size(size):
    sizing = None
    if size == "256x256":
        sizing = "256x256"
    elif size == "512x512":
        sizing = "512x512"
    elif size == "1024x1024":
        sizing = "1024x1024"
    return sizing

def openAi(prompt_in, engines, max_tokens):
    max_tokens = select_max_tokens(256)
    completion = openai.Completion.create(engine=modules(engines), prompt=prompt_in, temperature=0, max_tokens=select_max_tokens(max_tokens), top_p=1.0)
    result = completion.choices[0].text
    if len(result) < 150:
        sg.Popup('Responding...', keep_on_top=True)
        print(result)
        logger.info(result)
    else:
        sg.Popup('Responding to answers.txt', keep_on_top=True)
        print(result)
        with open('answers.txt', 'a+') as f:
            f.write(result)

def dalle(prompt_ins, size):
    response = openai.Image.create(
        prompt=prompt_ins,
        n=1,
        size=picture_size(size)
    )
    image_url = response['data'][0]['url']
    webUrl = urllib.request.urlopen(image_url)
    img = Image.open(webUrl)
    sg.Popup('Displaying and saving image...', keep_on_top=True)
    file_name = os.path.basename(prompt_ins)[:255] + '.png'
    img.show()
    img.save(file_name)

def make_window(theme):
    sg.theme(theme)
    max_tokens = select_max_tokens(256)
    # GUI layout.
    layout = [
        [sg.Text("OpenAIGUI", size=(63, 1), expand_x=True, expand_y=True, justification="center", font=(
            "Helvetica", 13), relief=sg.RELIEF_RIDGE, key="-TEXT HEADING-", enable_events=True)],
        [sg.TabGroup([
            [sg.Tab("OpenAi", [
                [sg.Radio("Choose model", "RADIO1", key="modules"), sg.Combo(
                    ["text-davinci-003", "text-davinci-002", "text-curie-001", "text-babbage-001", "text-ada-001"], key="engines")],
                [sg.Radio("Choose max token", "RADIO1", key="select_max_tokens"), sg.Combo(
                    [256, 2000, 8000], key="max_tokens")],
                [sg.Text("Enter your question or statement below:",
                         font=("Arial", 9, 'bold'))],
                [sg.Multiline(key="prompt", size=(77, 20),
                              expand_x=True, expand_y=True)],
                [sg.Multiline(size=(60, 15), font=("Arial", 9), expand_x=True, expand_y=True, write_only=True,
                              reroute_stdout=True, reroute_stderr=True, echo_stdout_stderr=True, autoscroll=True, auto_refresh=True)],
                [sg.Button("Answer"), sg.Button('Open file'),
                 sg.Button("Clear"), sg.Button("Quit")]
            ]),
                sg.Tab("Dall-E", [
                    [sg.Text("Suggest impression:", font=("Arial", 9, 'bold'))],
                    [sg.Radio("Choose picture size", "RADIO1", key="picture_size"), sg.Combo(
                        ["256x256", "512x512", "1024x1024"], key="size")],
                    [sg.Multiline(key="promptdalle", size=(
                        77, 20), expand_x=True, expand_y=True)],
                    [sg.Button("Create image"), sg.Button(
                     "Clear"), sg.Button("Quit")]
                ]),
                sg.Tab("Theme", [
                    [sg.Text("Choose theme:")],
                    [sg.Listbox(values=sg.theme_list(), size=(20, 12),
                                key="-THEME LISTBOX-", enable_events=True)],
                    [sg.Button("Set Theme")]
                ]),
                sg.Tab("About", [
                    [sg.Text(
                        "text-davinci-003 - Upgraded davinci-002. GPT3 chatbot model.")],
                    [sg.Text(
                        "text-davinci-002 - Code review, complex intent, cause and effect, summarization for audience")],
                    [sg.Text(
                        "code-davinci-edit-001 - Edit endpoint is particularly useful for editing code.")],
                    [sg.Text(
                        "text-curie-001 - Language translation, complex classification, text sentiment, summarization")],
                    [sg.Text(
                        "text-babbage-001 - Moderate classification, semantic search classification")],
                    [sg.Text(
                        "text-ada-001 - Parsing text, simple classification, address correction, keywords")]
                ])
            ]], key="-TAB GROUP-", expand_x=True, expand_y=True)
         ]]
    layout[-1].append(sg.Sizegrip())
    # Gui window and layout sizing.
    # icon='C:/icon.ico'
    window = sg.Window('OpenAI GUI', layout, resizable=True,
                       return_keyboard_events=True, finalize=True)
    return window

# GUI window that runs the main() function to interact with the user.
def main():
    window = make_window(sg.theme())
    # Event loop.
    while True:
        event, values = window.read(timeout=100)
        max_tokens = select_max_tokens(377)
        if values is not None:
            engines = values['engines'] if values['engines'] == 'Choose model' else values['engines']
        if values is not None:
            max_tokens = values['max_tokens'] if values['max_tokens'] == 'Choose max token' else values['max_tokens']
        if values is not None:
            size = values['size'] if values['size'] == 'Choose picture size' else values['size']
        if event == 'Answer':
            prompt_in = values['prompt']
            openAi(prompt_in, engines, max_tokens)
        elif event == 'Create image':
            prompt_ins = values['promptdalle']
            dalle(prompt_ins, size)
        elif event == 'Open file':
            os.startfile('answers.txt', 'open')
        elif event == 'Clear':
            window['prompt'].update('')
        elif event == "Set Theme":
            theme_chosen = values['-THEME LISTBOX-'][0]
            window.close()
            window = make_window(theme_chosen)
            sg.popup(f"Chosen Theme: {str(theme_chosen)}", keep_on_top=True)
        elif event == sg.WINDOW_CLOSED or event == 'Quit':
            break

    window.close()
    sys.exit(0)

if __name__ == '__main__':
    sg.theme('black')
    sg.theme('dark red')
    sg.theme('dark green 7')
    main()
    
