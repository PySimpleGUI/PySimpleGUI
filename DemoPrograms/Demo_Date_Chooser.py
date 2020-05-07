import PySimpleGUI as sg
import datetime
import calendar
import itertools

"""
    Demo_Date_Chooser
    
    This is the same code that is now used internally in PySimpleGUI as the 'date chooser'
    It is shown here in a demo program form to demonstrate to you that PySimpleGUI is being used
    to implement user features.  The underlying GUI framework is no longer being used like it was previously
    
    Copyright 2020 PySimpleGUI
"""


def popup_get_date(start_mon=None, start_day=None, start_year=None, begin_at_sunday_plus=0, no_titlebar=True, title='Choose Date', keep_on_top=True, location=(None, None), close_when_chosen=False, icon=None, locale=None, month_names=None, day_abbreviations=None):
    """
    Display a calendar window, get the user's choice, return as a tuple (mon, day, year)

    :param start_mon: The starting month
    :type start_mon: int
    :param start_day: The starting day - optional. Set to None or 0 if no date to be chosen at start
    :type start_day: int or None
    :param start_year: The starting year
    :type start_year: int
    :param begin_at_sunday_plus: Determines the left-most day in the display. 0=sunday, 1=monday, etc
    :type begin_at_sunday_plus: int
    :param icon: Same as Window icon parameter. Can be either a filename or Base64 value. For Windows if filename, it MUST be ICO format. For Linux, must NOT be ICO
    :type icon: str
    :param locale: locale used to get the day names
    :type locale: str
    :param month_names: optional list of month names to use (should be 12 items)
    :type month_names: List[str]
    :param day_abbreviations: optional list of abbreviations to display as the day of week
    :type day_abbreviations: List[str]
    :return: Tuple containing (month, day, year) of chosen date or None if was cancelled
    :rtype: None or (int, int, int)
    """

    if month_names is not None and len(month_names) != 12:
        sg.popup_error('Incorrect month names list specified. Must have 12 entries.', 'Your list:', month_names)

    if day_abbreviations is not None and len(day_abbreviations) != 7:
        sg.popup_error('Incorrect day abbreviation list. Must have 7 entries.', 'Your list:', day_abbreviations)

    day_font = 'TkFixedFont 9'
    mon_year_font = 'TkFixedFont 10'
    arrow_font = 'TkFixedFont 7'

    now = datetime.datetime.now()
    cur_month, cur_day, cur_year = now.month, now.day, now.year
    cur_month = start_mon or cur_month
    if start_mon is not None:
        cur_day = start_day
    else:
        cur_day = cur_day
    cur_year = start_year or cur_year


    def update_days(window, month, year, begin_at_sunday_plus):
        [window[(week, day)].update('') for day in range(7) for week in range(6)]
        weeks = calendar.monthcalendar(year, month)
        month_days = list(itertools.chain.from_iterable([[0 for _ in range(8 - begin_at_sunday_plus)]] + weeks))
        if month_days[6] == 0:
            month_days = month_days[7:]
            if month_days[6] == 0:
                month_days = month_days[7:]
        for i, day in enumerate(month_days):
            offset = i
            if offset >= 6 * 7:
                break
            window[(offset // 7, offset % 7)].update(str(day) if day else '')

    def make_days_layout():
        days_layout = []
        for week in range(6):
            row = []
            for day in range(7):
                row.append(sg.T('', size=(4, 1), justification='c', font=day_font, key=(week, day), enable_events=True, pad=(0, 0)))
            days_layout.append(row)
        return days_layout


    # Create table of month names and week day abbreviations

    if day_abbreviations is None or len(day_abbreviations) != 7:
        fwday = calendar.SUNDAY
        try:
            if locale is not None:
                _cal = calendar.LocaleTextCalendar(fwday, locale)
            else:
                _cal = calendar.TextCalendar(fwday)
            day_names = _cal.formatweekheader(3).split()
        except Exception as e:
            print('Exception building day names from locale', locale,  e)
            day_names = ('Sun', 'Mon', 'Tue', 'Wed', 'Th', 'Fri', 'Sat')
    else:
        day_names = day_abbreviations

    mon_names = month_names if month_names is not None and len(month_names) == 12  else [calendar.month_name[i] for i in range(1,13)]
    days_layout = make_days_layout()

    layout = [[sg.B('◄◄', font=arrow_font, border_width=0, key='-YEAR-DOWN-', pad=((10,2),2)),
                sg.B('◄', font=arrow_font, border_width=0, key='-MON-DOWN-', pad=(0,2)),
               sg.Text('{} {}'.format(mon_names[cur_month - 1], cur_year), size=(16, 1), justification='c', font=mon_year_font, key='-MON-YEAR-', pad=(0,2)),
               sg.B('►', font=arrow_font,border_width=0, key='-MON-UP-', pad=(0,2)),
               sg.B('►►', font=arrow_font,border_width=0, key='-YEAR-UP-', pad=(2,2))]]
    layout += [[sg.Col([[sg.T(day_names[i - (7 - begin_at_sunday_plus) % 7], size=(4,1), font=day_font, background_color=sg.theme_text_color(), text_color=sg.theme_background_color(), pad=(0,0)) for i in range(7)]], background_color=sg.theme_text_color(), pad=(0,0))]]
    layout += days_layout
    if not close_when_chosen:
        layout += [[sg.Button('Ok', border_width=0,font='TkFixedFont 8'), sg.Button('Cancel',border_width=0, font='TkFixedFont 8')]]

    window = sg.Window(title, layout, no_titlebar=no_titlebar, grab_anywhere=True, keep_on_top=keep_on_top, font='TkFixedFont 12', use_default_focus=False, location=location, finalize=True, icon=icon)

    update_days(window, cur_month, cur_year, begin_at_sunday_plus)

    prev_choice = chosen_mon_day_year = None

    if cur_day:
        chosen_mon_day_year = cur_month, cur_day, cur_year
        for week in range(6):
            for day in range(7):
                if window[(week,day)].DisplayText == str(cur_day):
                    window[(week,day)].update(background_color=sg.theme_text_color(), text_color=sg.theme_background_color())
                    prev_choice = (week,day)
                    break

    while True:             # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            chosen_mon_day_year = None
            break
        if event == 'Ok':
            break
        if event in ('-MON-UP-', '-MON-DOWN-', '-YEAR-UP-','-YEAR-DOWN-'):
            cur_month += (event == '-MON-UP-')
            cur_month -= (event == '-MON-DOWN-')
            cur_year += (event == '-YEAR-UP-')
            cur_year -= (event == '-YEAR-DOWN-')
            if cur_month > 12:
                cur_month = 1
                cur_year += 1
            elif cur_month < 1:
                cur_month = 12
                cur_year -= 1
            window['-MON-YEAR-'].update('{} {}'.format(mon_names[cur_month - 1], cur_year))
            update_days(window, cur_month, cur_year, begin_at_sunday_plus)
            if prev_choice:
                window[prev_choice].update(background_color=sg.theme_background_color(), text_color=sg.theme_text_color())
        elif type(event) is tuple:
            if window[event].DisplayText != "":
                chosen_mon_day_year = cur_month, int(window[event].DisplayText), cur_year
                if prev_choice:
                    window[prev_choice].update(background_color=sg.theme_background_color(), text_color=sg.theme_text_color())
                window[event].update(background_color=sg.theme_text_color(), text_color=sg.theme_background_color())
                prev_choice = event
                if close_when_chosen:
                    break
    window.close()
    return chosen_mon_day_year


print(popup_get_date())