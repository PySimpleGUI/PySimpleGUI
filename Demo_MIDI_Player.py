#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
import os
import mido
import time
import sys

PLAYER_COMMAND_NONE = 0
PLAYER_COMMAND_EXIT = 1
PLAYER_COMMAND_PAUSE = 2
PLAYER_COMMAND_NEXT = 3
PLAYER_COMMAND_RESTART_SONG = 4

# ---------------------------------------------------------------------- #
#    PlayerGUI             CLASS                                         #
# ---------------------------------------------------------------------- #
class PlayerGUI():
    '''
    Class implementing GUI for both initial screen but the player itself
    '''

    def __init__(self):
        self.Window = None
        self.TextElem = None
        self.PortList = mido.get_output_names()        # use to get the list of midi ports
        self.PortList = self.PortList[::-1]            # reverse the list so the last one is first

    # ---------------------------------------------------------------------- #
    #  PlayerChooseSongGUI                                                   #
    #   Show a GUI get to the file to playback                               #
    # ---------------------------------------------------------------------- #
    def PlayerChooseSongGUI(self):

        # ---------------------- DEFINION OF CHOOSE WHAT TO PLAY GUI ----------------------------

        layout = [[sg.Text('MIDI File Player', font=("Helvetica", 15), size=(20, 1), text_color='green')],
                  [sg.Text('File Selection', font=("Helvetica", 15), size=(20, 1))],
                  [sg.Text('Single File Playback', justification='right'), sg.InputText(size=(65, 1), key='midifile'), sg.FileBrowse(size=(10, 1), file_types=(("MIDI files", "*.mid"),))],
                  [sg.Text('Or Batch Play From This Folder', auto_size_text=False, justification='right'), sg.InputText(size=(65, 1), key='folder'), sg.FolderBrowse(size=(10, 1))],
                  [sg.Text('_' * 250, auto_size_text=False, size=(100, 1))],
                  [sg.Text('Choose MIDI Output Device', size=(22, 1)),
                   sg.Listbox(values=self.PortList, size=(30, len(self.PortList) + 1), key='device')],
                  [sg.Text('_' * 250, auto_size_text=False, size=(100, 1))],
                  [sg.SimpleButton('PLAY', size=(12, 2), button_color=('red', 'white'), font=("Helvetica", 15), bind_return_key=True), sg.Text(' ' * 2, size=(4, 1)), sg.Cancel(size=(8, 2), font=("Helvetica", 15))]]

        window = sg.Window('MIDI File Player', auto_size_text=False, default_element_size=(30, 1), font=("Helvetica", 12)).Layout(layout)
        self.Window = window
        return window.Read()


    def PlayerPlaybackGUIStart(self, NumFiles=1):
        # -------  Make a new FlexForm  ------- #

        image_pause = './ButtonGraphics/Pause.png'
        image_restart = './ButtonGraphics/Restart.png'
        image_next = './ButtonGraphics/Next.png'
        image_exit = './ButtonGraphics/Exit.png'

        self.TextElem = sg.T('Song loading....', size=(70, 5 + NumFiles), font=("Helvetica", 14), auto_size_text=False)
        self.SliderElem = sg.Slider(range=(1, 100), size=(50, 8), orientation='h', text_color='#f0f0f0')
        layout = [
                    [sg.T('MIDI File Player', size=(30, 1), font=("Helvetica", 25))],
                    [self.TextElem],
                    [self.SliderElem],
                    [sg.Button('', button_color=sg.TRANSPARENT_BUTTON,
                                       image_filename=image_pause, image_size=(50,50), image_subsample=2, border_width=0, key='PAUSE'), sg.T(' '),
                     sg.Button('', button_color=sg.TRANSPARENT_BUTTON,
                                       image_filename=image_next, image_size=(50,50), image_subsample=2, border_width=0, key='NEXT'), sg.T(' '),
                     sg.Button('', button_color=sg.TRANSPARENT_BUTTON,
                                       image_filename=image_restart, image_size=(50,50), image_subsample=2, border_width=0, key='Restart Song'), sg.T(' '),
                     sg.Button('', button_color=sg.TRANSPARENT_BUTTON,
                                     image_filename=image_exit, image_size=(50,50), image_subsample=2, border_width=0,key='EXIT')]
                  ]

        window = sg.Window('MIDI File Player', default_element_size=(30, 1), font=("Helvetica", 25)).Layout(layout).Finalize()
        self.Window = window



    # ------------------------------------------------------------------------- #
    #  PlayerPlaybackGUIUpdate                                                  #
    #   Refresh the GUI for the main playback interface (must call periodically #
    # ------------------------------------------------------------------------- #
    def PlayerPlaybackGUIUpdate(self, DisplayString):
        window = self.Window
        if 'window' not in locals() or window is None:          # if the widnow has been destoyed don't mess with it
            return PLAYER_COMMAND_EXIT
        self.TextElem.Update(DisplayString)
        event, (values) = window.Read(timeout=0)
        if event is None:
            return PLAYER_COMMAND_EXIT
        if event == 'PAUSE':
            return PLAYER_COMMAND_PAUSE
        elif event == 'EXIT':
            return PLAYER_COMMAND_EXIT
        elif event == 'NEXT':
            return PLAYER_COMMAND_NEXT
        elif event == 'Restart Song':
            return PLAYER_COMMAND_RESTART_SONG
        return PLAYER_COMMAND_NONE


# ---------------------------------------------------------------------- #
# MAIN - our main program... this is it                                  #
#   Runs the GUI to get the file / path to play                          #
#   Decodes the MIDI-Video into a MID file                               #
#   Plays the decoded MIDI file                                          #
# ---------------------------------------------------------------------- #
def main():
    def GetCurrentTime():
        '''
        Get the current system time in milliseconds
        :return: milliseconds
        '''
        return int(round(time.time() * 1000))


    pback = PlayerGUI()

    button, values = pback.PlayerChooseSongGUI()
    if button != 'PLAY':
        sg.PopupCancel('Cancelled...\nAutoclose in 2 sec...', auto_close=True, auto_close_duration=2)
        sys.exit(69)
    if values['device']:
        midi_port = values['device'][0]
    else:
        sg.PopupCancel('No devices found\nAutoclose in 2 sec...', auto_close=True, auto_close_duration=2)

    batch_folder = values['folder']
    midi_filename = values['midifile']
    # ------ Build list of files to play --------------------------------------------------------- #
    if batch_folder:
        filelist = os.listdir(batch_folder)
        filelist = [batch_folder+'/'+f for f in filelist if f.endswith(('.mid', '.MID'))]
        filetitles = [os.path.basename(f) for f in filelist]
    elif midi_filename:       # an individual filename
        filelist = [midi_filename,]
        filetitles = [os.path.basename(midi_filename),]
    else:
        sg.PopupError('*** Error - No MIDI files specified ***')
        sys.exit(666)

    # ------ LOOP THROUGH MULTIPLE FILES --------------------------------------------------------- #
    pback.PlayerPlaybackGUIStart(NumFiles=len(filelist) if len(filelist) <=10 else 10)
    port = None
    # Loop through the files in the filelist
    for now_playing_number, current_midi_filename in enumerate(filelist):
        display_string = 'Playing Local File...\n{} of {}\n{}'.format(now_playing_number+1, len(filelist), current_midi_filename)
        midi_title = filetitles[now_playing_number]
        # --------------------------------- REFRESH THE GUI ----------------------------------------- #
        pback.PlayerPlaybackGUIUpdate(display_string)

        # ---===--- Output Filename is .MID --- #
        midi_filename = current_midi_filename

        # --------------------------------- MIDI - STARTS HERE ----------------------------------------- #
        if not port:            # if the midi output port not opened yet, then open it
            port = mido.open_output(midi_port if midi_port else None)

        try:
            mid = mido.MidiFile(filename=midi_filename)
        except:
            print('****** Exception trying to play MidiFile filename = {}***************'.format(midi_filename))
            sg.PopupError('Exception trying to play MIDI file:', midi_filename, 'Skipping file')
            continue

        # Build list of data contained in MIDI File using only track 0
        midi_length_in_seconds = mid.length
        display_file_list = '>> ' + '\n'.join([f for i, f in enumerate(filetitles[now_playing_number:]) if i < 10])
        paused = cancelled = next_file = False
        ######################### Loop through MIDI Messages ###########################
        while(True):
            start_playback_time = GetCurrentTime()
            port.reset()

            for midi_msg_number, msg in enumerate(mid.play()):
                #################### GUI - read values ##################
                if not midi_msg_number % 4:              # update the GUI every 4 MIDI messages
                    t = (GetCurrentTime() - start_playback_time)//1000
                    display_midi_len = '{:02d}:{:02d}'.format(*divmod(int(midi_length_in_seconds),60))
                    display_string = 'Now Playing {} of {}\n{}\n              {:02d}:{:02d} of {}\nPlaylist:'.\
                        format(now_playing_number+1, len(filelist), midi_title, *divmod(t, 60), display_midi_len)
                     # display list of next 10 files to be played.
                    pback.SliderElem.Update(t, range=(1,midi_length_in_seconds))
                    rc = pback.PlayerPlaybackGUIUpdate(display_string + '\n' + display_file_list)
                else:       # fake rest of code as if GUI did nothing
                    rc = PLAYER_COMMAND_NONE
                if paused:
                    rc = PLAYER_COMMAND_NONE
                    while rc == PLAYER_COMMAND_NONE:        # TIGHT-ASS loop waiting on a GUI command
                        rc = pback.PlayerPlaybackGUIUpdate(display_string)
                        time.sleep(.25)

                ####################################### MIDI send data ##################################
                port.send(msg)

                # -------  Execute GUI Commands  after sending MIDI data ------- #
                if rc == PLAYER_COMMAND_EXIT:
                    cancelled = True
                    break
                elif rc == PLAYER_COMMAND_PAUSE:
                    paused = not paused
                    port.reset()
                elif rc == PLAYER_COMMAND_NEXT:
                    next_file = True
                    break
                elif rc == PLAYER_COMMAND_RESTART_SONG:
                    break

            if cancelled or next_file:
                break
        #------- DONE playing the song   ------- #
        port.reset()                    # reset the midi port when done with the song

        if cancelled:
            break

# ---------------------------------------------------------------------- #
#  LAUNCH POINT -- program starts and ends here                          #
# ---------------------------------------------------------------------- #
if __name__ == '__main__':
    main()

