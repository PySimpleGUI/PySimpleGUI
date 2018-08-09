import PySimpleGUI as sg

def MachineLearningGUI():
    sg.SetOptions(text_justification='right')
    form = sg.FlexForm('Machine Learning Front End', font=("Helvetica", 12))  # begin with a blank form

    layout = [[sg.Text('Machine Learning Command Line Parameters', font=('Helvetica', 16))],
              [sg.Text('Passes', size=(15, 1)), sg.Spin(values=[i for i in range(1, 1000)], initial_value=20, size=(6, 1)),
               sg.Text('Steps', size=(18, 1)), sg.Spin(values=[i for i in range(1, 1000)], initial_value=20, size=(6, 1))],
              [sg.Text('ooa', size=(15, 1)), sg.In(default_text='6', size=(10, 1)), sg.Text('nn', size=(15, 1)), sg.In(default_text='10', size=(10, 1))],
              [sg.Text('q', size=(15, 1)), sg.In(default_text='ff', size=(10, 1)), sg.Text('ngram', size=(15, 1)), sg.In(default_text='5', size=(10, 1))],
              [sg.Text('l', size=(15, 1)), sg.In(default_text='0.4', size=(10, 1)), sg.Text('Layers', size=(15, 1)), sg.Drop(values=('BatchNorm', 'other'),auto_size_text=True)],
              [sg.Text('_' * 100, size=(65, 1))],
              [sg.Text('Flags', font=('Helvetica', 15), justification='left')],
              [sg.Checkbox('Normalize', size=(12, 1), default=True), sg.Checkbox('Verbose', size=(20, 1))],
              [sg.Checkbox('Cluster', size=(12, 1)), sg.Checkbox('Flush Output', size=(20, 1), default=True)],
              [sg.Checkbox('Write Results', size=(12, 1)), sg.Checkbox('Keep Intermediate Data', size=(20, 1))],
              [sg.Text('_' * 100, size=(65, 1))],
              [sg.Text('Loss Functions', font=('Helvetica', 15), justification='left')],
              [sg.Radio('Cross-Entropy', 'loss', size=(12, 1)), sg.Radio('Logistic', 'loss', default=True, size=(12, 1))],
              [sg.Radio('Hinge', 'loss', size=(12, 1)), sg.Radio('Huber', 'loss', size=(12, 1))],
              [sg.Radio('Kullerback', 'loss', size=(12, 1)), sg.Radio('MAE(L1)', 'loss', size=(12, 1))],
              [sg.Radio('MSE(L2)', 'loss', size=(12, 1)), sg.Radio('MB(L0)', 'loss', size=(12, 1))],
              [sg.Submit(), sg.Cancel()]]
    button, values = form.LayoutAndRead(layout)
    del(form)
    sg.SetOptions(text_justification='left')

    return button, values


def CustomMeter():

    progress_bar = sg.ProgressBar(10000, orientation='h', size=(20,20))

    layout = [[sg.Text('A custom progress meter')],
              [progress_bar],
              [sg.Cancel()]]

    form = sg.FlexForm('Custom Progress Meter')
    form.LayoutAndRead(layout, non_blocking=True)

    for i in range(10000):
        button, values = form.ReadNonBlocking()
        progress_bar.UpdateBar(i)


if __name__ == '__main__':
    CustomMeter()
    MachineLearningGUI()
