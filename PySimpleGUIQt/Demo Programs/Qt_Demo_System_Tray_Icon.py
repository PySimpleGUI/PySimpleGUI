"""
    Demonstrates how to use a window in conjunction with a system tray icon to simulate the typical
    windows program that uses the system tray

    When the window is showing, there is no system tray icon shown.
    When closing the window with X button, the system tray is activated
    Clicking the "Minimize to Tray" button causes the window to disappear and the tray icon to appear
    Double clicking tray icon causes window to re-appear
    Choosing "Restore" from system tray right click menu will retore the window
"""

logo = b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAtCAMAAADbYcjNAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAMAUExURQAAADBpmDFqmDBqmTFqmjJrmzJsmzJsnDNtnTRrmjVtmjZsmzRunTRunjVvnzdwnjVwnzpxnzVwoDZxoTdyojlyoThzozhzpDh0pDp1pjp2pj51ozt3qDt4qDx4qDx5qj16qj57rD58rT98rkF1oEB4pUB4pkR6pkJ6qEN8q0B9rUB9rkB+rkV7qUZ8qUp9p0x+p0h/rEB+sEeArkqArEqBr0uCrkKAsUKAskOCs0OCtESCtEWEtkaFuEaGuE2FsUiHukiIukmJvEmKvEqLvkuMvk2KuUyLvEyMv1OErVWDqlWHr1qHrVaIsVCMvFSPvV2LsViOuVSQvmyUtmyXuXKbvXefv3ugv06NwE6OwFmUwl2XxGScyGmbw22hynikxnmmyv/UO//UPP/VPf/UPv/VP//UQP/VQf/VQv/WQP/WQf/WQv/WQ//XRP/WRf/WSf/YRf/YRv/YR//YSP/ZSf/ZSv/aS//aTP/aTf/bTv/YUf/ZUv/bUP/cUP/cUv/dVP/dVv/eVv/bW//dWf/cWv/eWP/fWv/dXf/fXf/eXv/cYP/fYP/dZP/dZv/eZf/fZv/eaP/gW//gXP/gXv/gYP/iYf/iYv/hZP/jZP/iZv/kZv/jaf/ja//kaP/lav/kbP/lb//mbP/mbv/ncP/mcv/iff/ocv/odP/odv/oeP/of//qf4GnxYOox4SoxYSpx4asyo+ux4isyouuyouvzIyuyYyvy4yvzI6wy46wzIyz0pCuyJSxyZWyy5u3zZ24zpW30pG52J250J+60aC60KS90aDC3a3E163F2K3F2bPI2bvO3rzP3qvJ4LHN4rnR5P/qgf/qgv/qiP/sif/sjf/sj//olf/ql//ulv/omf/qnv/tnP/qoP/ro//qpP/sov/upf/tqP/uqP/vrf/vrv/us//wpP/wpv/xrf/wsP/wsv/ys//xtP/ytf/ytv/zuf/zuv/0vP/0vsDS38XZ6cnb6f/xw//zwv/yxf/1w//zyP/1yf/2zP/3z//30wAAAM55ho4AAAEAdFJOU////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////wBT9wclAAAACXBIWXMAABcQAAAXEAEYYRHbAAAAGHRFWHRTb2Z0d2FyZQBwYWludC5uZXQgNC4xLjFjKpxLAAADnElEQVRIS62OeVhUZRSHw6IosQzGBgoIszKXqGylghKwbHErNVPbEFQQTXYogzZtt2SmiSEHnBHJPdM2Ldv3xbW91Pay0tT29dc53znfvTP809Pz9P7x3Xvu8773fHvhP/M/JBce0GX/8/WduX3ipDt/1nclNrk4TnhR5y1FVzHX/KqzISY5Uou4uLVm/sgEzF1mFqKTruozL9D8gfrM1aIwbvJaF7WFJ4FJqgtb1XOTN1R1eBqYrLbwvpo2+SF2B/NEbFNY+IWoNum6t0UD4imgTO3CCROKiqaJqsnx8fHx+7ho/RBALsnFxcUlJSWlNxpXkkv2I/a1uPnLWEA626WlU6aUlf3uJomJiccdlJDAoQvFBwPsklw2deq06dNnO8nIbj3oHE4hkWDQ7HVcSzLb5eXlFRWVTtKj+/P8OJDojfO6Wahfi3uMW1FZWVVVVV39jk2Skl6RR9JhwOjunDJUPYfZ1q6uqampvcUmWZ4sOpcnJ9Pj8WQqHYAZ4tbW1tXV19ffbJNXPZ6sUUM8nqOBRzweT7LDBQDZdcYmZlz3rk2wNCUlxes9iXYcwlBmOAq4W12moeE2liXBg9QcA6yiB+P1eqk8FtgmdoOh8SbjaoJlqacAj6ZqYqBffCJyo+GGO0S1CVYDKw8VUg0nAJ87NnOrmk4CPJYmSNeHdjQ2Xm/kmcx9qkUlKzKU9PT0tLSTaYeVZ84i/KpFJQ9nZmYermRknAh8qu6sOU1EUDXCJit6UuJwFu1gm+WmJp/PR7f6xr9NVE2eOYLoaeEdVvb5/H7/XOC7QCDwoXE16d+L4IzpC3xmZLb99wYC9wPbm5mP2ZVkRH9DP0OvK/CLcUkmmpvn0Y5gsKWlJRRykwEOXAJBI5NNBNtoRyhEJxa3bnKS005ltBoAqGz+3E47Qq2tO9gLR+jQJAbaItdgWhdje1tbOPwHe5GFdEhyuiE7O1sTkQ1t4fZwOBKJbCTt6/lfOsllZ0TzE9rZpV8bORKZz2z46q2ODpYlwZmCJFfiTyuL3WHZzK4ma7QRgJ2dZcG4mmBoriEnJ4eSc4BvO9vMe0a1CQZKIwwDdqkWxRIxnWT9QOJsITd3KN1NRRc1nQTrzs3L40y4CNitprLwbxXdBD/mM3nCWPoQs+cBkYioBLi8oMBk+flcAHtUJ942HwwxCd4cM2hQATFO5+81WPSbfmBiE+Cl8ZcOHvusDsBfG+hKm/foJHRO/hXgH831bVAP1oP5AAAAAElFTkSuQmCC'


import PySimpleGUIQt as sg

# create and then hide the tray icon
menu_def = ['My Menu Def', ['&Restore', '&Open', '&Save',['1', '2', ['a','b']], '&Properties', 'E&xit']]
tray = sg.SystemTray('Title', menu=menu_def, data_base64=logo)
tray.Hide()

# create the window
layout = [
    [sg.Text('Tray Icon Demo') ],
    [sg.Button('Minimize to Tray')]
        ]
window = sg.Window('My window').Layout(layout)

tray_visible = False
window_visible = True
window_closed = False
while True:     # the event loop
    # do normal window operations
    if window_visible:
        event, values = window.Read()
        print(event)
        if event is None:       # if window closed with X
            tray.UnHide()
            tray_visible = True
            window_visible = False
            window_closed = True
        elif event == 'Minimize to Tray':
            print('Minimizing to tray')
            window.Hide()
            tray.UnHide()
            tray_visible = True
            window_visible = False
        elif event == 'Message':
            tray.ShowMessage('Title of message', 'This is a tray message')
    # do tray icon stuff.  Tray events will cause the window.Read call to return with a Timeout event
    if tray_visible:
        menu_item = tray.Read()
        if menu_item == 'Restore' or menu_item == sg.EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED:
            print('Restoring')
            tray.Hide()
            tray_visible = False
            window_visible = True
            # If the window was completely closed, must get a BRAND NEW WINDOW MADE from scratch. No re-use allowed
            if window_closed:
                window_closed = False
                layout = [
                    [sg.Text('Tray Icon Demo')],
                    [sg.Button('Minimize to Tray')]
                ]
                window = sg.Window('My window').Layout(layout)
            else:
                window.UnHide()
        else:           # some other tray command was received
            print('Menu item %s'%menu_item)
            if menu_item == 'Exit':
                break

