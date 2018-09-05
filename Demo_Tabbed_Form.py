import PySimpleGUI as sg

def eBaySuperSearcherGUI():
    # Drop Down list of options
    configs = ('0 - Gruen - Started 2 days ago in Watches',
               '1 - Gruen - Currently Active in Watches',
               '2 - Alpina - Currently Active in Jewelry',
               '3 - Gruen - Ends in 1 day in Watches',
               '4 - Gruen - Completed in Watches',
               '5 - Gruen - Advertising',
               '6 - Gruen - Currently Active in Jewelry',
               '7 - Gruen - Price Test',
               '8 - Gruen - No brand name specified')

    us_categories = ('Use Default with no change',
                     'All - 1',
                     'Jewelry - 281',
                     '   Watches - 14324',
                     '        Wristwatches - 31387',
                     '        Pocket Watches - 3937',
                     'Advertising - 34',
                     '    Watch Ads - 165254'
                     )

    german_categories =('Use Default with no change',
                        'All - 1',
                        'Jewelry - 281',
                        '   Watches - 14324',
                        '        Wristwatches - 31387',
                        '        Pocket Watches - 3937',
                        'Advertising - 1',
                        '    Watch Ads - 19823'
                        )


    # the form layout
    with sg.FlexForm('EBay Super Searcher', auto_size_text=True) as form:
        with sg.FlexForm('EBay Super Searcher', auto_size_text=False) as form2:
            layout_tab_1 = [[sg.Text('eBay Super Searcher!', size=(60,1), font=('helvetica', 15))],
              [sg.Text('Choose base configuration to run')],
              [sg.InputCombo(configs)],
              [sg.Text('_'*100, size=(80,1))],
              [sg.InputText(),sg.Text('Choose Destination Folder'), sg.FolderBrowse(target=(sg.ThisRow,0))],
              [sg.InputText(),sg.Text('Custom text to add to folder name')],
              [sg.Text('_'*100, size=(80,1))],
              [sg.Checkbox('US', default=True, size=(15, 1)), sg.Checkbox('German', size=(15, 1), default=True, )],
              [sg.Radio('Active Listings','ActiveComplete', default = True,size=(15, 1)), sg.Radio('Completed Listings', 'ActiveComplete', size=(15, 1))],
              [sg.Text('_'*100, size=(80,1))],
              [sg.Checkbox('Save Images', size=(15,1)),sg.Checkbox('Save PDFs', size=(15,1)), sg.Checkbox('Extract PDFs', size=(15,1))],
              [sg.Text('_'*100, size=(80,1))],
               [sg.Text('Time Filters')],
               [sg.Radio('No change','time', default=True),sg.Radio('ALL listings','time'),sg.Radio('Started 1 day ago','time', size=(15,1)),sg.Radio('Started 2 days ago','time', size=(15,1)), sg.Radio('Ends in 1 day','time', size=(15,1))],
               [sg.Text('_'*100, size=(80,1))],
              [sg.Text('Price Range'), sg.InputText(size=(10,1)),sg.Text('To'), sg.InputText(size=(10,1))],
              [sg.Text('_'*100, size=(80,1))],
              [sg.Submit(button_color=('red', 'yellow')), sg.Cancel(button_color=('white', 'blue'))]]


            # First category is default (need to special case this)
            layout_tab_2 = [[sg.Text('Choose Category')],
                       [sg.Text('US Categories'),sg.Text('German Categories')],
                       [sg.Radio(us_categories[0],'CATUS', default=True), sg.Radio(german_categories[0], 'CATDE', default=True)]]

            for i,cat in enumerate(us_categories):
                if i == 0: continue         # skip first one
                layout_tab_2.append([sg.Radio(cat,'CATUS'), sg.Radio(german_categories[i],'CATDE')])

            layout_tab_2.append([sg.Text('_' * 100, size=(75, 1))])
            layout_tab_2.append([sg.Text('US Search String Override')])
            layout_tab_2.append([sg.InputText(size=(100,1))])
            layout_tab_2.append([sg.Text('German Search String Override')])
            layout_tab_2.append([sg.InputText(size=(100,1))])
            layout_tab_2.append([sg.Text('Typical US Search String')])
            layout_tab_2.append([sg.InputText(size=(100,1), default_text='gruen -sara -quarz -quartz -embassy -bob -robert -elephants -adidas -LED ')])
            layout_tab_2.append([sg.Text('_' * 100, size=(75, 1))])
            layout_tab_2.append([sg.Submit(button_color=('red', 'yellow')), sg.Cancel(button_color=('white', 'blue'))])

            results = sg.ShowTabbedForm('eBay Super Searcher', (form,layout_tab_1,'Where To Save'), (form2, layout_tab_2, 'Categories & Search String'))

    return results


if __name__ == '__main__':
    # sg.SetOptions(background_color='white')
    results = eBaySuperSearcherGUI()
    print(results)
    sg.MsgBox('Results', results)