import make_real_readme as mk_readme
import PySimpleGUI as sg
import logging, os 

enable_logs = False

def readfile(filename):
    with open(filename, 'r', encoding='utf-8') as ff:
        return ff.read()

def writefile(fpath, content):
    with open(fpath, 'w', encoding='utf-8') as ff:
        ff.write(content)
    
        
window = sg.Window('Test',     [
    [sg.CB('include all .md files', True, key='all-checkbox', enable_events=True)],
    [sg.CB('1', True, key='file1', disabled=True, enable_events=True)],
    [sg.CB('2', False,key='file2', disabled=True, enable_events=True)],
    [sg.CB('3', False,key='file3', disabled=True, enable_events=True)],


    [sg.CB('4', False,key='file4', disabled=True, enable_events=True)],
    [sg.T('well, this is you output name:'), sg.I('readme.md', key='output_name'), sg.B('aaaand, hope for the best... Compile.', key='comp')],
    
    [sg.T('-- -- -- -- -- -- --\nlogs\n-- -- -- -- -- -- --', justification='center')],
    # [sg.ML('', key='logs', size=(120,25))]

    [sg.Column([
        [sg.T('COMPLETE')],
        [sg.Listbox([], size=(40, 10), key='COMPLETE')]
    ]), sg.Column([
        [sg.T('NOTCOMPLETE')],
        [sg.Listbox([], size=(40, 10), key='NOTCOMPLETE')]
    ])],

],element_justification='center')

while True:
    event, values = window()
    if event in ('Exit', None): break

    print(event, values)

    if event == 'all-checkbox':
        window['file1'](disabled=values['all-checkbox'])
        window['file2'](disabled=values['all-checkbox'])
        window['file3'](disabled=values['all-checkbox'])
        window['file4'](disabled=values['all-checkbox'])
    if event == 'comp':
        
        if enable_logs: window['logs'](values['logs'] + 'start')

        # MAIN WORK - START
        # 1### logging module
        logger = logging.getLogger(__name__); logger.setLevel(logging.DEBUG); a_log_file = logging.FileHandler('_logs.txt', mode='w'); a_log_file.setLevel(logging.DEBUG); formatter = logging.Formatter('%(asctime)s>%(levelname)s: %(message)s'); a_log_file.setFormatter(formatter); logger.addHandler(a_log_file);
        # 2### files to compile
        files = [0, 1, 2, 3] if values['all-checkbox'] else []
        if not values['all-checkbox']:
            if values['file1']: files.append(1)
            if values['file2']: files.append(2)
            if values['file3']: files.append(3)
            if values['file4']: files.append(4)
        # 3### REAL work:
        mk_readme.main(logger=logger,
                files_to_include=files,
                output_name=values['output_name'],
                delete_html_comments=True)

        # MAIN WORK - END

        for i in readfile('_logs.txt').split('\n'):
            if i.endswith('--> - COMPLETE'):
                window['COMPLETE'](values['COMPLETE'] + [i])
            else:
                window['NOTCOMPLETE'](values['COMPLETE'] + [i])

        if enable_logs: window['logs'](values['logs'] + output_readme)




window.close()