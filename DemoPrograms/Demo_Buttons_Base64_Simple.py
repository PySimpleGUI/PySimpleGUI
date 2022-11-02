import PySimpleGUI as sg
"""
    Demo - Base64 Buttons with Images

    This is perhaps the easiest, quickest, and safest way to use buttons with images in PySimpleGUI.
    By putting the button into your code, then you only have to distribute a single file.
    
    Copyright 2022 PySimpleGUI
"""

# First the button images

play = b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAByElEQVRoge3ZMWsUQRjG8Z8RFSKCgoJp0qSJjVpoZ2clkk8g5CtYpU+TD5DSUkvbVCFNYiM2dhZqY6GFQooEISGai8Xu4HgmcnM3c+su+4fj2L2dmedhb+Z95x16enp6hljBxaZF5OAE7/GoaSGTchJ9tnCrWTnjE0zs19+HWMPlJkWNQzAyh2c4rq+/YBnnmpOWRjASuIfX0f0d3GlAVzLDRmBG9Ta+1r8d4wVuTFdaGqcZCVzFOn7Uz+ziKc5PR1oa/zISWMRm9OxbPCisK5lRjASW8Clqs4H5MrLSSTECs1jFQd3ue319KbewVFKNBBbwMmr/EY8z6kpmXCOBh3gX9dNYdjCpEbigWs326r6OVKvdlQn7TSKHkcCcKt4MNJAd5DQSuI83Ud87uJ15jL8oYYTf2cE3f2YH1wuMhXJGAtdU8+WnwtlBaSOBu3gVjZc9O5iWEapJ/wSf6zEHeI6bZzWYmY6u/4v+rzUirZ/snVh+hwPitpYFxNanKJ1IGk9L4xcz6Eom18bqg5ZtrDqx1Y2LDwPVG2lV8aH15aDWF+jOKpkWi8o5GKWIXTwq56BzxwqdOejpxNFbJw5DO3M83dPT02J+AbN50HbYDxzCAAAAAElFTkSuQmCC'
stop = b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAAaklEQVRoge3ZQQqAMAxFwSre/8p6AZFUiXzKzLqLPNJVOwYAvLcVzpztU9Q8zrr/NUW3Y+JsZXsdSjdimY0ISSMkjZA0QtIISSMkjZA0QtIISSMkjZA0QtIISSMkzcxrfMo/ya1lNgIAX1zq+ANHUjXZuAAAAABJRU5ErkJggg=='
eject = b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAByklEQVRoge3YO2gUURSA4S+JRnyACIGADyxERAsb0UKrWIidWIidlSA2YpFWSauNVtrYiIU2YpFCLGwEEWwsBAsLEbFQFARFfKBZizkyK5pkZvZmZ7PeH05z595z/sPszpxdMplMJpMZbDZFLGsm8CxiomWXxqzBQ3QiHmNdq0YNGMc9RQOvIjqxNt6iVy1GcF0h/h47sR1vY+0mRluzq8ElhfBn7O9a34tPce1KC161OK8Q/Y7D/7h+EF9jz7k+etXilELwJ44vsO8ofsTeM33wqsURpdzZCvtPK5s+toRetZjCF4XYTI1zM3HmGw4lt6rJbnxQCF1tcP5ynP2IPQm9arENb0LkDsYa5BjFrcjxDjuS2VVkI16EwH2s6iHXStxVvjy39GxXkfV4Iu3Y0T3OPMWGBDkXZDUeRMHnmEyY+/eA2cEjrE2Y+w/GcDsKvcbWJaixGS+jxixWpC4wgmvK+WlX6gJddM9lN6J2Mi4q56cDKRPPwz7lXHYhVdJp5W+KtmK61yZOYG4AGpnDyV6byWT+ZxZ7Rnf6YlGdeX2XxZ8AVag6AiR9uzZg0U/G0NyR3MigUfU7MmhPr78YmjuSyWQymUxmmPgFokSdfYSQKDwAAAAASUVORK5CYII='

sg.theme('Light Green 3')

# Define the window's layout
layout = [[sg.Button(image_data=play, key='-PLAY-',  button_color=sg.theme_background_color(), border_width=0),
           sg.Button(image_data=stop, key='-STOP-',  button_color=sg.theme_background_color(), border_width=0),
           sg.Button(image_data=eject, key='-EXIT-',  button_color=sg.theme_background_color(), border_width=0)]  ]

# Create the window
window = sg.Window('Simple Base64 Buttons', layout)

while True:                             # Event Loop
    event, values = window.read()       # type: str, dict
    print(event, values)
    if event in (sg.WIN_CLOSED, '-EXIT-'):         # If the user exits
        break
window.close()          # Exiting so clean up
