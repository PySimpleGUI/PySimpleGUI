#!/usr/bin/env python
import PySimpleGUI as sg
import csv
import os
import operator

"""
    Demo - Simple CSV Table Display
    
    Enables you to easily filter and sort tables that are in a CSV file format
    
    Choose your CSV file and then a table will be displayed.
    Clicking on a heading will sort on that column if no value is entered for the filter.
    If a filter value is entered and then a heading is clicked, then only rows matchines the filter in that column as are displayed
        The filtering is not case sensative so no need to worry about exact matches 
    Use the checkbox to specify ascending or descending sorting
    
    The first row in your table needs to be the Column Names
    
    Copyright 2022 PySimpleGUI
"""

sg.theme('Dark gray 13')

CSV_FILE = sg.popup_get_file('CSV File to Display', file_types=(("CSV Files", "*.csv"),), initial_folder=os.path.dirname(__file__), history=True)
if CSV_FILE is None:
    sg.popup_error('Canceling')
    exit()

csv.field_size_limit(2147483647)        # enables huge tables

def sort_table(table, cols, descending=False):
    """ sort a table by multiple columns
        table: a list of lists (or tuple of tuples) where each inner list
               represents a row
        cols:  a list (or tuple) specifying the column numbers to sort by
               e.g. (1,0) would sort by column 1, then by column 0
    """

    for col in reversed(cols):
        try:
            table = sorted(table, key=operator.itemgetter(col), reverse=descending)
        except Exception as e:
            sg.popup_error('Error in sort_table', 'Exception in sort_table', e)
    return table


def read_csv_file(filename):
    data = []
    header_list = []
    if filename is not None:
        try:
            with open(filename, encoding='UTF-16') as infile:
                reader = csv.reader(infile,delimiter='\t')
                # reader = fix_nulls(filename)
                header_list = next(reader)
                try:
                    data = list(reader)  # read everything else into a list of rows
                except Exception as e:
                    print(e)
                    sg.popup_error('Error reading file', e)
                    return None, None
        except:
            with open(filename,  encoding='utf-8') as infile:
                reader = csv.reader(infile, delimiter=',')
                # reader = fix_nulls(filename)
                header_list = next(reader)
                try:
                    data = list(reader)  # read everything else into a list of rows
                except Exception as e:
                    with open(filename) as infile:
                        reader = csv.reader(infile, delimiter=',')
                        # reader = fix_nulls(filename)
                        header_list = next(reader)
                        try:
                            data = list(reader)  # read everything else into a list of rows
                        except Exception as e:
                            print(e)
                            sg.popup_error('Error reading file', e)
                            return None, None
    return data, header_list


def main():
    data, header_list = read_csv_file(CSV_FILE)

    sg.popup_quick_message('Building your main window.... one moment....', background_color='#1c1e23', text_color='white', keep_on_top=True, font='_ 30')

    # ------ Window Layout ------
    layout = [  [sg.Text('Click a heading to sort on that column or enter a filter and click a heading to search for matches in that column')],
                [sg.Text(f'{len(data)} Records in table', font='_ 18')],
                [sg.Text(k='-RECORDS SHOWN-', font='_ 18')],
                [sg.Text(k='-SELECTED-')],
                [sg.T('Filter:'), sg.Input(k='-FILTER-', focus=True, tooltip='Not case sensative\nEnter value and click on a col header'),
                 sg.B('Reset Table', tooltip='Resets entire table to your original data'),
                 sg.Checkbox('Sort Descending', k='-DESCENDING-'), sg.Checkbox('Filter Out (exclude)', k='-FILTER OUT-', tooltip='Check to remove matching entries when filtering a column'), sg.Push()],
                [sg.Table(values=data, headings=header_list, max_col_width=25,
                        auto_size_columns=True, display_row_numbers=True, vertical_scroll_only=True,
                        justification='right', num_rows=50,
                        key='-TABLE-', selected_row_colors='red on yellow', enable_events=True,
                        expand_x=True, expand_y=True,
                        enable_click_events=True)],
                [sg.Sizegrip()]]

    # ------ Create Window ------
    window = sg.Window('CSV Table Display', layout, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT,  resizable=True, finalize=True)
    window.bind("<Control_L><End>", '-CONTROL END-')
    window.bind("<End>", '-CONTROL END-')
    window.bind("<Control_L><Home>", '-CONTROL HOME-')
    window.bind("<Home>", '-CONTROL HOME-')
    original_data = data        # save a copy of the data
    # ------ Event Loop ------
    while True:
        event, values = window.read()
        # print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if values['-TABLE-']:           # Show how many rows are slected
            window['-SELECTED-'].update(f'{len(values["-TABLE-"])} rows selected')
        else:
            window['-SELECTED-'].update('')
        if event[0] == '-TABLE-':
        # if isinstance(event, tuple):
            filter_value = values['-FILTER-']
            # TABLE CLICKED Event has value in format ('-TABLE=', '+CLICKED+', (row,col))
            if event[0] == '-TABLE-':
                if event[2][0] == -1 and event[2][1] != -1:  # Header was clicked and wasn't the "row" column
                    col_num_clicked = event[2][1]
                    # if there's a filter, first filter based on the column clicked
                    if filter_value not in (None, ''):
                        filter_out = values['-FILTER OUT-']     # get bool filter out setting
                        new_data = []
                        for line in data:
                            if not filter_out and (filter_value.lower() in line[col_num_clicked].lower()):
                                new_data.append(line)
                            elif filter_out and (filter_value.lower() not in line[col_num_clicked].lower()):
                                new_data.append(line)
                        data = new_data
                    new_table = sort_table(data, (col_num_clicked, 0), values['-DESCENDING-'])
                    window['-TABLE-'].update(new_table)
                    data = new_table
                    window['-RECORDS SHOWN-'].update(f'{len(new_table)} Records shown')
                    window['-FILTER-'].update('')           # once used, clear the filter
                    window['-FILTER OUT-'].update(False)  # Also clear the filter out flag
        elif event == 'Reset Table':
            data = original_data
            window['-TABLE-'].update(data)
            window['-RECORDS SHOWN-'].update(f'{len(data)} Records shown')
        elif event == '-CONTROL END-':
            window['-TABLE-'].set_vscroll_position(100)
        elif event == '-CONTROL HOME-':
            window['-TABLE-'].set_vscroll_position(0)
        elif event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Version':
            sg.popup_scrolled(__file__, sg.get_versions(), location=window.current_location(), keep_on_top=True, non_blocking=True)
    window.close()


if __name__ == '__main__':
    main()
