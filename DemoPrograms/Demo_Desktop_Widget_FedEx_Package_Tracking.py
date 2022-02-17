import requests
import PySimpleGUI as sg
import datetime

"""
    Demo - FedEx Package Tracking
    
    A simple Desktop Widget that checks your FedEx tracking number and
    shows the current delivery estimate.
    
    USING:
        Enter a tracking number in the input element
        Right click and choose Refresh
        If additional tracking numbers are desired, right click and choose Add Package
    
    The status information is courtesy of @israel-dryer (https://github.com/israel-dryer)
    He used web scraping to gather the data.  This removes the need for using an account and access package.
    
    At the moment only FedEx is supported.  The drop-down list is there for future support of other carriers.
    
    Like other PySimpleGUI Desktop Widgets, a number of standard features are include such as:
        * Alpha Channel
        * Theme Selection
        * Screen location
        * Edit Me (launcher your editor for easy code modification)
    
    Copyright 2021 PySimpleGUI, Israel Dryer
"""

def choose_theme(location):
    layout = [[sg.Text(f'Current theme {sg.theme()}')],
              [sg.Listbox(values=sg.theme_list(), size=(20, 20), key='-LIST-', enable_events=True)],
              [sg.OK(), sg.Cancel()]]

    window = sg.Window('Look and Feel Browser', layout, location=location, keep_on_top=True, no_titlebar=True)
    old_theme = sg.theme()
    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit', 'OK', 'Cancel'):
            break
        sg.theme(values['-LIST-'][0])
    window.close()

    if event == 'OK' and values['-LIST-']:
        sg.theme(values['-LIST-'][0])
        sg.user_settings_set_entry('-theme-', values['-LIST-'][0])
        return values['-LIST-'][0]
    else:
        sg.theme(old_theme)
    return  None


def shipping_status(tracking_num):
    """Request shipment status via tracking number.
    Args:
        tracking_num (str): The FedEx tracking number assigned to the shipment.
    """
    url = "https://www.fedex.com/trackingCal/track"
    headers = {
        'Host': 'www.fedex.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.fedex.com',
        'Connection': 'keep-alive',
        'Referer': 'https://www.fedex.com/en-us/home.html',
        }
    payload = '''data=%7B%22TrackPackagesRequest%22%3A%7B%22appType%22%3A%22WTRK%22%2C%22appDeviceType%22%3A%22%22%2C%22supportHTML%22%3Atrue%2C%22supportCurrentLocation%22%3Atrue%2C%22uniqueKey%22%3A%22%22%2C%22processingParameters%22%3A%7B%7D%2C%22trackingInfoList%22%3A%5B%7B%22trackNumberInfo%22%3A%7B%22trackingNumber%22%3A%22{}%22%2C%22trackingQualifier%22%3A%22%22%2C%22trackingCarrier%22%3A%22%22%7D%7D%5D%7D%7D&action=trackpackages&locale=en_US&version=1&format=json'''

    response = requests.post(url, headers=headers, data=payload.format(tracking_num))
    if response.status_code == 200:
        return response.json()
    else:
        return (None, response.status_code)


def package_row(item_num, tracking_num=''):
    carrier_list = ('FedEx', 'USPS')
    tracking_numbers = sg.user_settings_get_entry('-packages-', [])
    row =  [sg.pin(sg.Col([[sg.B(sg.SYMBOL_X, border_width=0, button_color=(sg.theme_text_color(), sg.theme_background_color()), k=('-DEL-', item_num), tooltip='Delete this item'),
                            sg.Combo(tracking_numbers, default_value=tracking_num, size=(20, 1), key=('-ID-', item_num)),
                            sg.In(size=(20,1), k=('-DESC-', item_num)),
                 # sg.Input(default_text=tracking_num, s=(20,1), key=('-ID-', item_num), tooltip='Enter your package ID'),
                            sg.Combo(carrier_list, default_value=carrier_list[0], readonly=True, s=(10,10), k=('-CARRIER-', item_num), tooltip='Not implemented'), sg.T(size=(15,1), k=('-STATUS-', item_num))]], k=('-ROW-', item_num)))]
    return row


def refresh(window: sg.Window):
    row_count = window.metadata+1
    # make and save package list. ID, Description,
    package_list = []
    for row in range(row_count):
        if not window[('-ROW-', row)].visible:    # skip deleted rows
            continue
        status = shipping_status(window[('-ID-', row)].get())
        single_package = (window[('-ID-', row)].get(), window[('-DESC-', row)].get())
        package_list.append(single_package)
        if isinstance(status, tuple):           # an error occured
            delivery_datetime = 'Error'
        else:
            delivery_datetime = status['TrackPackagesResponse']['packageList'][0]['displayEstDeliveryDateTime']
        window[('-STATUS-', row)].update(delivery_datetime)
    window['-REFRESHED-'].update(f'Refreshed {datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")}')
    sg.user_settings_set_entry('-packages-', package_list)


def add_packages_to_window(window: sg.Window):
    packages = sg.user_settings_get_entry('-packages-', [])
    for i, package in enumerate(packages):
        in_elem = window.find_element(('-ID-', i), silent_on_error=True)
        if isinstance(in_elem, sg.ErrorElement):
            window.metadata += 1
            window.extend_layout(window['-TRACKING SECTION-'], [package_row(window.metadata)])
            in_elem = window.find_element(('-ID-', window.metadata), silent_on_error=True)
            in_elem.update(package[0])
        else:
            in_elem.update(package[0])
        desc_elem = window.find_element(('-DESC-', i), silent_on_error=True)
        if not isinstance(desc_elem, sg.ErrorElement):
            desc_elem.update(package[1])

def make_window(location):
    location =  sg.user_settings_get_entry('-location-',location)
    alpha = sg.user_settings_get_entry('-alpha-', 0.9)

    layout = [  [sg.Text('FedEx Package Tracking', font='_ 15')],
                [sg.Col([package_row(0)], k='-TRACKING SECTION-')],
                [sg.pin(sg.Text(size=(35,1), font='_ 8', k='-REFRESHED-',))],
                [sg.T(sg.SYMBOL_X, enable_events=True, k='Exit', tooltip='Exit Application'), sg.T('↻', enable_events=True, k='Refresh',  tooltip='Save Changes & Refresh'), sg.T('+', enable_events=True, k='Add Package', tooltip='Add Another Package')]]

    right_click_menu = [[''], ['Add Package',  'Edit Me', 'Change Theme', 'Save Location', 'Refresh', 'Alpha', [str(x) for x in range(1, 11)], 'Exit', ]]

    window = sg.Window('Window Title', layout, finalize=True, no_titlebar=True, grab_anywhere=True, keep_on_top=True,
                       right_click_menu=right_click_menu, alpha_channel=alpha, location=location, use_default_focus=False, font='_ 15', metadata=0)
    add_packages_to_window(window)

    return window


def main():
    theme = sg.user_settings_get_entry('-theme-', 'Dark Gray 14')
    sg.theme(theme)
    location =  sg.user_settings_get_entry('-location-', (None, None))

    window = make_window(location)
    refresh(window)
    while True:
        event, values = window.read(timeout=1000*60*60)     # wake every hour
        if event == sg.WIN_CLOSED or event == 'Exit':
            if event == 'Exit':
                sg.user_settings_set_entry('-location-', window.current_location())
            break
        if event == 'Add Package':
            window.metadata += 1
            window.extend_layout(window['-TRACKING SECTION-'], [package_row(window.metadata)])
        elif event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Save Location':
            sg.user_settings_set_entry('-location-', window.current_location())
        elif event == 'Change Theme':
            loc = window.current_location()
            if choose_theme(loc) is not None:
                _, window = window.close(), make_window(loc)
        elif event in ('Refresh', sg.TIMEOUT_KEY):
            # Invert colors of simulated "button" (Text Element) while the refresh is happening
            window['Refresh'].update(text_color=sg.theme_text_element_background_color(), background_color=sg.theme_text_color())
            window.refresh()
            refresh(window)
            window['Refresh'].update(text_color=sg.theme_text_color(), background_color=sg.theme_text_element_background_color())
        elif event in [str(x) for x in range(1,11)]:
            window.set_alpha(int(event)/10)
            sg.user_settings_set_entry('-alpha-', int(event)/10)
        if isinstance(event, tuple):
            if event[0] == '-DEL-':
                window[('-ROW-', event[1])].update(visible=False)
                packages: list = sg.user_settings_get_entry('-packages-', [])
                try:
                    packages.remove(window[('-ID-', event[1])].get())
                except:
                    pass
                sg.user_settings_set_entry('-packages-', packages)
    window.close()


if __name__ == '__main__':
    main()
