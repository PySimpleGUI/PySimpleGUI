import PySimpleGUI as sg
import os
import base64

'''
    Base64 Encoder - encodes a folder of PNG files and creates a .py file with definitions
'''

OUTPUT_FILENAME = 'output.py'

def main():
    # folder = r'C:\Python\PycharmProjects\GooeyGUI\Uno Cards'
    folder=''
    folder = sg.PopupGetFolder('Source folder for images\nImages will be encoded and results saved to %s'%OUTPUT_FILENAME,
                               title='Base64 Encoder',
                               default_path=folder, initial_folder=folder )

    if folder is None or folder == '':
        sg.PopupCancel('Cancelled - No valid folder entered')
        return
    try:
        namesonly = [f for f in os.listdir(folder) if f.endswith('.png') or f.endswith('.ico')]
    except:
        sg.PopupCancel('Cancelled - No valid folder entered')
        return

    outfile = open(os.path.join(folder, OUTPUT_FILENAME), 'w')

    for i, file in enumerate(namesonly):
        contents = open(os.path.join(folder, file), 'rb').read()
        encoded = base64.b64encode(contents)
        outfile.write('\n{} = {}\n\n'.format(file[:file.index(".")], encoded))
        sg.OneLineProgressMeter('Base64 Encoding', i+1, len(namesonly),key='_METER_')

    outfile.close()
    sg.Popup('Completed!', 'Encoded %s files'%(i+1))


if __name__ == '__main__':
    main()
