import PySimpleGUI as sg
import datetime
import base64
from urllib import request
import json
import sys
import webbrowser

"""
    A Current Weather Widget

    Adapted from the weather widget originally created and published by Israel Dryer that you'll find here:
    https://github.com/israel-dryer/Weather-App

    BIG THANKS goes out for creating a good starting point for other widgets to be build from.

    A true "Template" is being developed that is a little more abstracted to make creating your own
    widgets easy.  Things like the settings window is being standardized, the settings file format too.

    You will need a key (APPID) from OpenWeathermap.org in order to run this widget. It's free, it's easy:
    https://home.openweathermap.org/

    Your initial location is determined using your IP address and will be used if no settings file is found

    This widget is an early version of a PSG Widget so it may not share the same names / constructs as the templates. 

    Copyright 2020, 2022 PySimpleGUI - www.PySimpleGUI.com

"""

SETTINGS_PATH = None            # use the default settings path (OS settings foloder)

API_KEY = ''  # Set using the "Settings" window and saved in your config file

sg.theme('Light Green 6')
ALPHA = 0.8

BG_COLOR = sg.theme_text_color()
TXT_COLOR = sg.theme_background_color()

APP_DATA = {
    'City': 'New York',
    'Country': 'US',
    'Postal': 10001,
    'Description': 'clear skys',
    'Temp': 101.0,
    'Feels Like': 72.0,
    'Wind': 0.0,
    'Humidity': 0,
    'Precip 1hr': 0.0,
    'Pressure': 0,
    'Updated': 'Not yet updated',
    'Icon': None,
    'Units': 'Imperial'
}


def load_settings():
    global API_KEY
    settings = sg.UserSettings(path=SETTINGS_PATH)
    API_KEY = settings['-api key-']
    if not API_KEY:
        sg.popup_quick_message('No valid API key found... opening setup window...', keep_on_top=True, background_color='red', text_color='white', auto_close_duration=3, non_blocking=False, location=win_location)
        change_settings(settings)
    return settings


def change_settings(settings, window_location=(None, None)):
    global APP_DATA, API_KEY

    try:
        nearest_postal = json.loads(request.urlopen('http://ipapi.co/json').read())['postal']
    except Exception as e:
        print('Error getting nearest postal', e)
        nearest_postal = ''

    layout = [[sg.T('Enter Zipcode or City for your location')],
              [sg.I(settings.get('-location-', nearest_postal), size=(15, 1), key='-LOCATION-'), sg.T('City')],
              [sg.I(settings.get('-country-', 'US'), size=(15, 1), key='-COUNTRY-'), sg.T('Country')],
              [sg.I(settings.get('-friends name-', ''), size=(15, 1), key='-FRIENDS NAME-'), sg.T('Who')],
              [sg.I(settings.get('-api key-', ''), size=(32, 1), key='-API KEY-')],
              [sg.CBox('Use Metric For Temperatures', default=settings.get('-celsius-', False),key='-CELSIUS-')],
              [sg.B('Ok', border_width=0, bind_return_key=True),  sg.B('Register For a Key', border_width=0, k='-REGISTER-'), sg.B('Cancel', border_width=0)], ]

    window = sg.Window('Settings', layout, location=window_location, no_titlebar=True, keep_on_top=True, border_depth=0)
    event, values = window.read()
    window.close()

    if event == '-REGISTER-':
        sg.popup('Launching browser so you can signup for the "Current Weather" service from OpenWeatherMap.org to get a Free API Key', 'Click OK and your browser will open', r'Visit https://home.openweathermap.org/ for more information', location=window_location)
        # Register to get a free key
        webbrowser.open(r'https://home.openweathermap.org/users/sign_up')


    if event == 'Ok':
        user_location = settings['-location-'] = values['-LOCATION-']
        settings['-country-'] = values['-COUNTRY-']
        API_KEY = settings['-api key-'] = values['-API KEY-']
        settings['-celsius-'] = values['-CELSIUS-']
        settings['-friends name-'] = values['-FRIENDS NAME-']
    else:
        API_KEY = settings['-api key-']
        user_location = settings['-location-']

    if user_location is not None:
        if user_location.isnumeric() and len(user_location) == 5 and user_location is not None:
            APP_DATA['Postal'] = user_location
            APP_DATA['City'] = ''
        else:
            APP_DATA['City'] = user_location
            APP_DATA['Postal'] = ''
    APP_DATA['Country'] = settings['-country-']
    if settings['-celsius-']:
        APP_DATA['Units'] = 'metric'
    else:
        APP_DATA['Units'] = 'imperial'

    return settings


def update_weather():
    if APP_DATA['City']:
        request_weather_data(create_endpoint(2))
    elif APP_DATA['Postal']:
        request_weather_data(create_endpoint(1))


def create_endpoint(endpoint_type=0):
    """ Create the api request endpoint
    {0: default, 1: zipcode, 2: city_name}"""
    if endpoint_type == 1:
        try:
            endpoint = f"http://api.openweathermap.org/data/2.5/weather?zip={APP_DATA['Postal']},{APP_DATA['Country']}&appid={API_KEY}&units={APP_DATA['Units']}"
            return endpoint
        except ConnectionError:
            return
    elif endpoint_type == 2:
        try:
            # endpoint = f"http://api.openweathermap.org/data/2.5/weather?q={APP_DATA['City'].replace(' ', '%20')},us&APPID={API_KEY}&units={APP_DATA['Units']}"
            endpoint = f"http://api.openweathermap.org/data/2.5/weather?q={APP_DATA['City'].replace(' ', '%20')},{APP_DATA['Country']}&APPID={API_KEY}&units={APP_DATA['Units']}"
            return endpoint
        except ConnectionError:
            return
    else:
        return


def request_weather_data(endpoint):
    """ Send request for updated weather data """
    global APP_DATA

    if endpoint is None:
        sg.popup_error('Could not connect to api.  endpoint is None', keep_on_top=True, location=win_location)
        return
    else:
        try:
            response = request.urlopen(endpoint)
        except request.HTTPError:
            sg.popup_error('ERROR Obtaining Weather Data',
                           'Is your API Key set correctly?',
                           API_KEY, keep_on_top=True, location=win_location)
            return
    if APP_DATA['Units'] == 'metric':
        temp_units, speed_units = '°C', 'm/sec'
    else:
        temp_units, speed_units = '°F', 'miles/hr'
    if response.reason == 'OK':
        weather = json.loads(response.read())
        APP_DATA['City'] = weather['name'].title()
        APP_DATA['Description'] = weather['weather'][0]['description']
        APP_DATA['Temp'] = "{:,.0f}{}".format(weather['main']['temp'], temp_units)
        APP_DATA['Humidity'] = "{:,d}%".format(weather['main']['humidity'])
        APP_DATA['Pressure'] = "{:,d} hPa".format(weather['main']['pressure'])
        APP_DATA['Feels Like'] = "{:,.0f}{}".format(weather['main']['feels_like'], temp_units)
        APP_DATA['Wind'] = "{:,.1f}{}".format(weather['wind']['speed'], speed_units)
        APP_DATA['Precip 1hr'] = None if not weather.get('rain') else "{:2} mm".format(weather['rain']['1h'])
        APP_DATA['Updated'] = 'Updated: ' + datetime.datetime.now().strftime("%B %d %I:%M:%S %p")
        APP_DATA['Lon'] = weather['coord']['lon']
        APP_DATA['Lat'] = weather['coord']['lat']

        icon_url = "http://openweathermap.org/img/wn/{}@2x.png".format(weather['weather'][0]['icon'])
        APP_DATA['Icon'] = base64.b64encode(request.urlopen(icon_url).read())


def metric_row(metric):
    """ Return a pair of labels for each metric """
    return [sg.Text(metric, font=('Arial', 10), pad=(15, 0), size=(9, 1)),
            sg.Text(APP_DATA[metric], font=('Arial', 10, 'bold'), pad=(0, 0), size=(9, 1), key=metric)]


def create_window(win_location, settings):
    """ Create the application window """
    friends_name = settings.get('-friends name-', '')
    col1 = sg.Column(
        [[sg.Text(APP_DATA['City'], font=('Arial Rounded MT Bold', 18),   background_color=BG_COLOR, text_color=TXT_COLOR, key='City'),
          sg.Text(f' - {friends_name}' if friends_name else '',  background_color=BG_COLOR, text_color=TXT_COLOR, font=('Arial Rounded MT Bold', 18),)],
         [sg.Text(APP_DATA['Description'], font=('Arial', 12), pad=(10, 0), background_color=BG_COLOR, text_color=TXT_COLOR, key='Description')]],
        background_color=BG_COLOR, key='COL1')

    col2 = sg.Column([[sg.Image(data=APP_DATA['Icon'], size=(100, 100), background_color=BG_COLOR, key='Icon')]],
                     element_justification='center', background_color=BG_COLOR, key='COL2')

    col3 = sg.Column([[sg.Text(APP_DATA['Updated'], font=('Arial', 8), background_color=BG_COLOR, text_color=TXT_COLOR, key='Updated')]],
                      pad=(10, 5), element_justification='left', background_color=BG_COLOR, key='COL3')

    col4 = sg.Column(
        [[sg.Text('Settings', font=('Arial', 8, 'italic'), background_color=BG_COLOR, text_color=TXT_COLOR, enable_events=True, key='-CHANGE-'),
          sg.Text('Refresh', font=('Arial', 8, 'italic'), background_color=BG_COLOR, text_color=TXT_COLOR, enable_events=True, key='-REFRESH-')]],
        pad=(10, 5), element_justification='right', background_color=BG_COLOR, key='COL4')

    top_col = sg.Column([[col1, sg.Push(background_color=BG_COLOR), col2, sg.Text('×', font=('Arial Black', 16), pad=(0, 0), justification='right', background_color=BG_COLOR, text_color=TXT_COLOR, enable_events=True, key='-QUIT-')]],                           pad=(0, 0), background_color=BG_COLOR, key='TopCOL')

    bot_col = sg.Column([[col3, col4]],
                        pad=(0, 0), background_color=BG_COLOR, key='BotCOL')

    lf_col = sg.Column(
        [[sg.Text(APP_DATA['Temp'], font=('Haettenschweiler', 90), pad=((10, 0), (0, 0)), justification='center', key='Temp')]],
        pad=(10, 0), element_justification='center', key='LfCOL')

    rt_col = sg.Column([metric_row('Feels Like'), metric_row('Wind'), metric_row('Humidity'), metric_row('Precip 1hr'), metric_row('Pressure')],
                        pad=((15, 0), (25, 5)), key='RtCOL')

    layout = [[top_col],
              [lf_col, rt_col],
              [bot_col],
              [sg.Text(f'PSG: {sg.ver} Tk:{sg.framework_version} Py:{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}', font=('Arial', 8), justification='c', background_color=BG_COLOR, text_color=TXT_COLOR, pad=(0,0), expand_x=True)]]

    window = sg.Window(layout=layout, title='Weather Widget', margins=(0, 0), finalize=True, location=win_location,
                       element_justification='center', keep_on_top=True, no_titlebar=True, grab_anywhere=True, alpha_channel=ALPHA,
                       right_click_menu=[[''], ['Edit Me', 'Versions', 'Exit',]], enable_close_attempted_event=True)

    for col in ['COL1', 'COL2', 'TopCOL', 'BotCOL', '-QUIT-']:
        window[col].expand(expand_y=True, expand_x=True)

    for col in ['COL3', 'COL4', 'LfCOL', 'RtCOL']:
        window[col].expand(expand_x=True)

    window['-CHANGE-'].set_cursor('hand2')
    window['-QUIT-'].set_cursor('hand2')
    window['-REFRESH-'].set_cursor('hand2')

    return window


def update_metrics(window):
    """ Adjust the GUI to reflect the current weather metrics """
    metrics = ['City', 'Temp', 'Feels Like', 'Wind', 'Humidity', 'Precip 1hr',
               'Description', 'Icon', 'Pressure', 'Updated']
    for metric in metrics:
        if metric == 'Icon':
            window[metric].update(data=APP_DATA[metric])
        else:
            window[metric].update(APP_DATA[metric])


def main(refresh_rate, win_location):
    """ The main program routine """
    refresh_in_milliseconds = refresh_rate * 60 * 1000

    # Load settings from config file. If none found will create one
    settings = load_settings()
    location = settings['-location-']
    APP_DATA['Country'] = settings.get('-country-', 'US')
    if settings.get('-celsius-'):
        APP_DATA['Units'] = 'metric'
    else:
        APP_DATA['Units'] = 'imperial'

    if location is not None:
        if location.isnumeric() and len(location) == 5 and location is not None:
            APP_DATA['Postal'] = location
            APP_DATA['City'] = ''
        else:
            APP_DATA['City'] = location
            APP_DATA['Postal'] = ''
        update_weather()
    else:
        sg.popup_error('Having trouble with location.  Your location: ', location)
        exit()

    window = create_window(win_location, settings)


    while True:  # Event Loop
        event, values = window.read(timeout=refresh_in_milliseconds)
        if event in (None, '-QUIT-', 'Exit', sg.WIN_CLOSE_ATTEMPTED_EVENT):
            sg.user_settings_set_entry('-win location-', window.current_location())  # The line of code to save the position before exiting
            break
        try:
            if event == '-CHANGE-':
                x, y = window.current_location()
                settings = change_settings(settings, (x + 200, y+50))
                window.close()
                window = create_window(win_location, settings)
            elif event == '-REFRESH-':
                sg.popup_quick_message('Refreshing...', keep_on_top=True, background_color='red', text_color='white',
                                       auto_close_duration=3, non_blocking=False, location=(window.current_location()[0]+window.size[0]//2-30, window.current_location()[1]+window.size[1]//2-10))
            elif event == 'Edit Me':
                sg.execute_editor(__file__)
            elif event == 'Versions':
                sg.main_get_debug_data()
            elif event != sg.TIMEOUT_KEY:
                sg.Print('Unknown event received\nEvent & values:\n', event, values, location=win_location)

            update_weather()
            update_metrics(window)
        except Exception as e:
            sg.Print('*** GOT Exception in event loop ***', c='white on red', location=window.current_location(), keep_on_top=True)
            sg.Print('File = ', __file__, f'Window title: {window.Title}')
            sg.Print('Exception = ', e, wait=True)      # IMPORTANT to add a wait/blocking so that the print pauses execution. Otherwise program continue and exits
    window.close()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        win_location = sys.argv[1].split(',')
        win_location = (int(win_location[0]), int(win_location[1]))
    else:
        win_location = sg.user_settings_get_entry('-win location-', (None, None))

    main(refresh_rate=1, win_location=win_location)