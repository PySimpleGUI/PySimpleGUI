import PySimpleGUI as sg

#
# An Async Demonstration of a media player
# Uses button images for a super snazzy look
# See how it looks here:
# https://user-images.githubusercontent.com/13696193/43159403-45c9726e-8f50-11e8-9da0-0d272e20c579.jpg
#
def MediaPlayerGUI():

    # Images are located in a subfolder in the Demo Media Player.py folder
    image_pause = './ButtonGraphics/Pause.png'
    image_restart = './ButtonGraphics/Restart.png'
    image_next = './ButtonGraphics/Next.png'
    image_exit = './ButtonGraphics/Exit.png'

    # A text element that will be changed to display messages in the GUI
    TextElem = sg.Text('', size=(15, 2), font=("Helvetica", 14))

    # Open a form, note that context manager can't be used generally speaking for async forms
    form = sg.FlexForm('Media File Player', auto_size_text=True, default_element_size=(20, 1),
                       font=("Helvetica", 25))
    # define layout of the rows
    layout= [[sg.Text('Media File Player',size=(17,1), font=("Helvetica", 25))],
            [TextElem],
             [sg.ReadFormButton('Restart Song', button_color=sg.TRANSPARENT_BUTTON,
                                image_filename=image_restart, image_size=(50, 50), image_subsample=2, border_width=0),
                                sg.Text(' ' * 2),
              sg.ReadFormButton('Pause', button_color=sg.TRANSPARENT_BUTTON,
                                image_filename=image_pause, image_size=(50, 50), image_subsample=2, border_width=0),
                                sg.Text(' ' * 2),
              sg.ReadFormButton('Next', button_color=sg.TRANSPARENT_BUTTON,
                                image_filename=image_next, image_size=(50, 50), image_subsample=2, border_width=0),
                                sg.Text(' ' * 2),
              sg.Text(' ' * 2), sg.SimpleButton('Exit', button_color=sg.TRANSPARENT_BUTTON,
                                                image_filename=image_exit, image_size=(50, 50), image_subsample=2, border_width=0)],
             [sg.Text('_'*30)],
             [sg.Text(' '*30)],
            [
             sg.Slider(range=(-10, 10), default_value=0, size=(10, 20), orientation='vertical', font=("Helvetica", 15)),
             sg.Text(' ' * 2),
             sg.Slider(range=(-10, 10), default_value=0, size=(10, 20), orientation='vertical', font=("Helvetica", 15)),
             sg.Text(' ' * 8),
             sg.Slider(range=(-10, 10), default_value=0, size=(10, 20), orientation='vertical', font=("Helvetica", 15))],
             [sg.Text('Bass', font=("Helvetica", 15), size=(6, 1)),
             sg.Text('Treble', font=("Helvetica", 15), size=(10, 1)),
             sg.Text('Volume', font=("Helvetica", 15), size=(7, 1))]

             ]

    # Call the same LayoutAndRead but indicate the form is non-blocking
    form.LayoutAndRead(layout, non_blocking=True)
    # Our event loop
    while(True):
        # Read the form (this call will not block)
        button, values = form.ReadNonBlocking()
        if button == 'Exit':
            break
        # If a button was pressed, display it on the GUI by updating the text element
        if button:
            TextElem.Update(button)

MediaPlayerGUI()

