"""
    Demo - Button Toggle #2


    Uses the IGNORE BUTTON setting.
    When creating or updating buttons in 4.35.0+, you can use the parameter:
        disabled=BUTTON_DISABLED_MEANS_IGNORE

    This will cause the buytton to ignore your clicks but it won't change the button
    with the GUI, which would change the color and gray it out.  The button will not
    change appearance at all. It will no longer respond to button clicks.

    Another toggle button using Base64 strings
    Of course files could be used instead of Base64 strings

    The differences between this toggle button demo and the other one are:
    1. Different button graphics
    2. The button state is stored in the metadata for the button
    3. The metadata for the button is a class instead of a single variable name

    For buttons with graphics, it's generally best to set the button's:
    * border width=0
    * color = (background_color, background_color)

    Buttons don't normally have explicit keys. However, since this button has
    no text, there is no default key. It's better to be explicit with buttons that
    change text or have graphics.

    Copyright 2021 PySimpleGUI
"""

import PySimpleGUI as sg
import random

# Class holding the button graphic info. At this time only the state is kept
class BtnInfo:
    def __init__(self, state=True):
        self.state = state        # Can have 3 states - True, False, None (disabled)

# Main function that creates the layout, window and has event loop
def main():
    layout = [[sg.Text('Toggle Button')],
              [sg.T('Disabled with PySimpleGUI Ignore:', text_color='yellow')],
              [sg.Button(image_data=on_image, k='-TOGGLE1-', border_width=0,
                         button_color=(sg.theme_background_color(), sg.theme_background_color()),
                         disabled_button_color=(sg.theme_background_color(), sg.theme_background_color()),
                         metadata=BtnInfo()),
               sg.T('Disable:'),
               sg.Button(image_data=off_image, k='-DISABLE1-', border_width=0,
                         button_color=(sg.theme_background_color(), sg.theme_background_color()),
                         disabled_button_color=(sg.theme_background_color(), sg.theme_background_color()),
                         metadata=BtnInfo(False)), sg.T('Disabled button color is\nbetter than other disabled button below')
               ],
              [sg.Button(image_data=on_image, k='-TOGGLE2-', border_width=0,
                         button_color=(sg.theme_background_color(), sg.theme_background_color()),
                         disabled_button_color=(sg.theme_background_color(), sg.theme_background_color()),
                         metadata=BtnInfo()),
               sg.Image(data=sg.EMOJI_BASE64_HAPPY_THUMBS_UP,enable_events=True, k='-I-')
               ],
              [ sg.T('Disabled with GUI:', text_color='yellow')],
              [sg.Button(image_data=on_image, k='-TOGGLE3-', border_width=0,
                         button_color=(sg.theme_background_color(), sg.theme_background_color()),
                         disabled_button_color=(sg.theme_background_color(), sg.theme_background_color()),
                         disabled=True, metadata=BtnInfo()), sg.T('Note color has crosshatching')],
              [ sg.T('Disabled with PySimpleGUI (ignored):', text_color='yellow')],
              [sg.Button(image_data=on_image, k='-TOGGLE4-', border_width=0,
                         button_color=(sg.theme_background_color(), sg.theme_background_color()),
                         disabled_button_color=(sg.theme_background_color(), sg.theme_background_color()),
                         disabled=sg.BUTTON_DISABLED_MEANS_IGNORE,
                         metadata=BtnInfo())],
              [sg.T(size=(40,1), k='-STATUS-')],
              [sg.Button('Exit')]]

    window = sg.Window('Window Title', layout, font='_ 14', finalize=True)

    while True:             # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        # Where all the magic happens. 2 things happen when button is clicked
        # 1. The state toggles
        # 2. The buton graphic changes
        if 'TOGGLE' in event:
            window[event].metadata.state = not window[event].metadata.state
            window[event].update(image_data=on_image if window[event].metadata.state else off_image)
        elif event == '-DISABLE1-':
            window[event].metadata.state = not window[event].metadata.state
            window[event].update(image_data=on_image if window[event].metadata.state else off_image)
            window['-I-'].update(data=sg.EMOJI_BASE64_HAPPY_GASP if window[event].metadata.state else random.choice(sg.EMOJI_BASE64_HAPPY_LIST))
            # if disabling the button
            if window[event].metadata.state:
                if window['-TOGGLE1-'].metadata.state is True:
                    window['-TOGGLE1-'].update(disabled=sg.BUTTON_DISABLED_MEANS_IGNORE, image_data=on_image_disabled)
                elif window['-TOGGLE1-'].metadata.state is False:
                    window['-TOGGLE1-'].update(disabled=sg.BUTTON_DISABLED_MEANS_IGNORE, image_data=off_image_disabled)
            else:
                if window['-TOGGLE1-'].metadata.state is True:
                    window['-TOGGLE1-'].update(disabled=False, image_data=on_image)
                elif window['-TOGGLE1-'].metadata.state is False:
                    window['-TOGGLE1-'].update(disabled=False, image_data=off_image)
        window['-STATUS-'].update(f'event {event} button state = {window[event].metadata.state if window[event].metadata is not None else "Not applicable"}')
    window.close()

# Define the button graphic base 64 strings and then call the main function
if __name__ == '__main__':
    on_image = b'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'

    off_image = b'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'

    off_image_disabled = b'iVBORw0KGgoAAAANSUhEUgAAAFoAAAAnCAYAAACPFF8dAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsIAAA7CARUoSoAAAAWJSURBVGhD7ZtLTyxFFMd7Bhgew2OAIXgDxkQWLgYWJsaNiTFxozcuiQs/gR9Bv4crXRuJG2OIiQvj1q25CZC4IQ4wL2B4zPCGwfqVcyaHTs371Xcu/+Sf6q6qnjr1r1PVVYcmtLGx4SmEotHoB7Ozs59GIpG3y3lBxIvj4+N/h4eHH2ZmZsbLeUFAqVgsvjo9Pf3t9vY2Vc6zqAg9Pj7+3srKyvexWOzjkZERz3TC5gcR9/f33t3dnXdycuIdHh56xjG8UChULu0fsGFiYsIbHR29TaVS3yWTyW9LpdKtLUNoI/Lq2tran9PT0wuGgRZZYDzGM57jGQ/ytra2rPj9wuPjY/nqf6ChcVrv8vLyj+3t7Zem/G5ofX09lEgkfp+bm1sx9MLhsH0QmtGoXAeBAjxnaGgIB7ECMwPNUmJtp6xXFPjzbm5uvHw+7y0vL79r7D4rFAp/hc1S8bkZgffNWmcrCURk0iBQbNGCIyx24yDmnWLzdKe7QQ1Xvlwz4/b29hD7G3MbRuhPMBIPEVCZ5QPiLUGg2IO4GmY9tLabfth73flukPaFkqfblWuAVxvb45OTkx+Gx8bG3nkd1uRaQGgGA0iH+0FpX9KHhwe7tBl942ZgwtO25DWH7mC/WAtP5+EAQE/tbrGayP5UY6CE1h3vBRHd1a5AXw+cR/s73Q2KV0t7jWDghO4VtPBadH2t8bx0tEAXquULnj26DdQTV2OghUYIjumcHBcWFmzwiXsN9uCcLl2UutFo9Ek+hyO5blTsgRUaARYXFy0J8ohYkicCITQD4KI50dk6PO8vY/DgGy/0/Py8Z069NpyazWZt3IGUk5p4uQb5mUzmCYkOahCWJT+dTleoYy+1MJBCs/0Sb8zlct7V1ZU9DpNyDyjX3ohg19fXT8ggaRAoIp/onNR5o4Um0AQQyiUW3ovIUg/4lxAJUmkwOFJGKhHDRjCQQounElZ1QbxQezSzQF5wQj9knUdoqAeqHvoqNB1uly6IwHipC3J01gOBl6dSqQpZf/3gjwtSfnBw4F1cXJRL6qMloV0dbpYSxG+XLrCGUkb417+d454BoH2WEQH1udf0g8HQ5dVmjAtPhNYdqMZuCqThesZFF8g/Pz+31+yfme4ITMo9oLza891A00LXg+uZZtnMYFYDW7NCoWCXCV5c7J1JuUfks7Ozcs3eoGmhe8FOgN9hTWUtJWUPTLq/v2//xCTtsBzwyQJ51SCfNchy0oqNFaGlk+2yHbh+rx7rge0dno0HkyKsBrOHlxp77Gpgv0wd9uIajbQvaOll6IJfgF5Rw1XeDfpRLV+jI0tHr16QQYLLbn2v80FHhG4Xrt9slH646nSa4ljSXiNoe+nQBvSDGq7ybhLBXe0K9HVFaI6j/gdqkUb6vWToI7RA7Oomq/XBn2ogdCXqwh5TP1yLnYDrd5uhPmJzL2k/yAC4IM4QNhVGJMIlXyzphztJtkearjqNkg5gL3ayZePYrW3vNQVyTYp9OINhPFwsFvfYiGMsxsu3bHRG/1Ar9IvjqtMK6QBBfcAel9+Wk56rfqdYrT+6XbkG8Xjc1jN78GRoc3Pzq0Qi8SOxVv4qIa4ulYMIsZFZcXR0ZKNpu7u7lahcr+DSSPKIrayurnLcv9zZ2XkrbE5Ev+ZyuT1ORhgtx0w6E1QCsZeYRjKZtPl0spfUkDwGm8CVcV6rZTab/cl4dUG++H+5tLS0GYvF+LrULh299o5mIGs88QeO1UxRGYB+AhskDItd+Xz+n3Q6/ZGx9ajyPyzRaPRLMxI/RCKRaf5EE1Sh8Rpe3qzNdEo+1w0CsA0HwJPNjPs7k8l8Ye4PKKsIDYy481NTU18b0T8zo/LCPz2eURvGo0tm9/PKvPx+MfzZZJW3zp73H5XujC+u8bu1AAAAAElFTkSuQmCC'
    on_image_disabled = b'iVBORw0KGgoAAAANSUhEUgAAAFoAAAAnCAYAAACPFF8dAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsIAAA7CARUoSoAAAAVLSURBVGhD7Zu7TytHFMbHyxvsJeb9kjCiCihRpJAobaqblFGUJmXqKMofkyZpaKhS5HaJIgUpRZQmoqAhSgEUSBZgsAE/uJhX5ht80LmH8e56fdde7PuTPu0yj/XMt7Nnd2aXxPr6uuKMjIx84LruR47jJGtJbeeVplQqOaOjo+8MDAwk7u7uyrWsWIF2FYvFf3Rbt/HnQ+oDj0Ynk8kPl5eXf9Amf6L7pW5vb9X9/b3Jaye5XE719fWpubk51dPTY/bjijba+KbN3t7d3f324uLir1rWg9HpdPrFysrKy0KhMJTNZtX19XUtu/0sLi6qyclJlUqlcLWpRCJRy4knNzc3ShusKpXKq52dnS/z+fyvSE9sbGxMrq2t/Xd8fJw+PDw0hf1oRWdxNY2Pj6tMJqMmJiZUf3//Y3ocrjQJPOG+nJ2dYWSXt7a23tMRYt+Zn5//rlqteppMB5EHi5rZ2VmEtEeTAUzGJRo3yZOv7ydo94j293v8ndjW6JDxvh7RpoBEGtsKo9FofdNTq6urampqSvX29tZynhcIIUdHR//qUb3iDA4OZnDzs0Gm0khulQCMBs/VZIC2Dw8Pv6v71OvoO7lri3nUYb5tlToRp7Z9Deos37ZanYbVaA7vON/qCU1k6kQC94oMhxFk+FuCU9doPnptkPFRqBN5YjTvKO1LE3iZtwSjMwNiDGnYaD6aEa/1czieFdXQ0JB1wQfPw5C8Cii9Wwg9omHw2NiYmSLDaCz4YNoJ8ScHpGNBCGU4SIe6hVBGY+0BBmOiUy6XzQIKpptY9cOohrESjHg+y+u2ON+w0TAXpgGYfHl5aZYGq9WqMRsLLDDbNnXGyelWQsVoisUwl4OTQGvZPF5TOsxHyOlGQsdogNEroTQZGkqlktkiLnfq7M+LpnpsM4zS5EIVXvFUKhVzAmC2zH+OoA/1JGnYaByEwoN8PONhBXFbgngOw1GvnaNamhJWjdBwb2EmDAP0/EwvTV3XNQbiRNDJ4KBxuIGGQXayGXlhKx9WnFDDCjdBGEZhIJ1Om+dnmI2RXCwWayWfgrpXV1e1v4IhG10P2dEwCoKtnpQkVOgAGNX5fN7c5LCP+IvHOzxT85sk0uUoxt+oh7ygyI7Y5IetTlSSNBUoYSheg8E4mCYf9wDy5asyqlfvFZrE1pFGhd+0pYdRPbzKPTGaF6B9WVEeJGro95uRH7Y6jcqLuiOaKvIDyP2oFBRb3bDywlbeT5LAocPvQFEif5sUBFu9RuVHkDq+RvOK/ECIeW8y7nHZsJULIj9sdRpVEKxGU2W+lftRywtb+bDywlY+qCTGaLkuAagw39pGcBSjWoJJkFe+hJdtRn7Y6kBAznwdZPCVNg5V4gegfS4KI29KgB4VMWVHo7nZtjpcvG1hZTuulK0eID/RdpQDjn7+PcfMrh5UGciDRiVA69w03UfjMdVHw9EB5EUp/IaXbHXQdrwUQTsB2q5nwZc6/T6xubn5WyaT+Wxvb08VCgVTwAtbmIkCNHpmZkYtLCyY76P5iwQ6GXGE/MHMFzPlg4ODP/f39z91Tk9Pfzw/P1dLS0tqenra10h0shUC+JQYbTs5OXltfQRtjKvQdhhMyuVyP5k244t/PXJ+0aPmCywM4dLEohAuD1S0QUa0ApiMD9LxMTrCB1SvXe0GnuHegi1M1m3/I5vNvtBZd8Zo3fCkNvvnZDL5OV41Ic7EqTM48RjReOdo+3QhLmAAwmis4ejQ8bu+Ir/SaWYpk/9XViKVSn3tuu43ujMf67t8975JDYk29UrfAP/WA2NdawNJDzlK/Q9RjPZ1HEiBtwAAAABJRU5ErkJggg=='

    main()