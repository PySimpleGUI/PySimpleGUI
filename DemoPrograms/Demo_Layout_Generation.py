import PySimpleGUI as sg

"""
    PySimpleGUI is designed & authored in Python to take full advantage the awesome Python constructs & capabilities.
    Layouts are represented as lists to PySimpleGUI. Lists are fundamental in Python and have a number of powerful
    capabilities that PySimpleGUI exploits.
       
    Many times PySimpleGUI programs can benefit from using CODE to GENERATE your layouts.  This Demo illustrates
    a number of ways of "building" a layout. Some work on 3.5 and up.  Some are basic and show concatenation of rows
    to build up a layout.  Some utilize generators.
    
    These 8 "Constructs" or Design Patterns demonstrate numerous ways of "generating" or building your layouts
    0 - A simple list comprehension to build a row of buttons
    1 - A simple list comprehension to build a column of buttons
    2 - Concatenation of rows within a layout
    3 - Concatenation of 2 complete layouts [[ ]] + [[ ]] = [[ ]]
    4 - Concatenation of elements to form a single row [ [] + [] + [] ] = [[ ]]
    5 - Questionnaire - Using a double list comprehension to build both rows and columns in a single line of code
    6 - Questionnaire - Unwinding the comprehensions into 2 for loops instead
    7 - Using the * operator to unpack generated items onto a single row 
    8 - Multiple Choice Test - a practical use showing list comprehension and concatenated layout
"""

"""
    Construct #0 - List comprehension to generate a row of Buttons

    Comprehensions are super-powers of Python.  In this example we're using a comprehension to create 4 buttons that
    are all on the same row.
"""


def layout0():
    layout = [[sg.Button(i) for i in range(4)]]     # A list of buttons is created

    window = sg.Window('Generated Layouts', layout)

    event, values = window.read()

    print(event, values)
    window.close()


"""
    Construct #1 - List comprehension to generate a Column of Buttons

    More list super-power, this time used to build a series of buttons doing DOWN the window instead of across

"""


def layout1():
    # a List of lists of buttons.  Notice the ] after Button
    layout = [[sg.Button(i)] for i in range(4)]

    window = sg.Window('Generated Layouts', layout)

    event, values = window.read()

    print(event, values)
    window.close()


"""
    Construct #2 - List comprehension to generate a row of Buttons and concatenation of more lines of elements

    Comprehensions are super-powers of Python.  In this example we're using a comprehension to create 4 buttons that
    are all on the same row, just like the previous example.
    However, here, we want to not just have a row of buttons, we want have an OK button at the bottom.
    To do this, you "add" the rest of the GUI layout onto the end of the generated part.
    
    Note - you can't end the layout line after the +. If you wanted to put the OK button on the next line, you need
    to add a \ at the end of the first line.
    See next Construct on how to not use a \ that also results in a VISUALLY similar to a norma layout
"""


def layout2():
    # if want to split, can't add newline after + to do it
    layout = [[sg.Button(i) for i in range(4)]] + [[sg.OK()]]

    window = sg.Window('Generated Layouts', layout)

    event, values = window.read()

    print(event, values)
    window.close()


"""
    Construct # 3 - Adding together what appears to be 2 layouts
    
    Same as layout2, except that the OK button is put on another line without using a \ so that the layout appears to
    look like a normal, multiline layout without a \ at the end
    
    Also shown is the OLD tried and true way, using layout.append.  You will see the append technique in many of the
    Demo programs and probably elsewhere.  Hoping to remove these and instead use this more explicit method of +=.
    
    Using the + operator, as you've already seen, can be used in the middle of the layout.  A call to append you cannot
    use this way because it modifies the layout list directly.
"""


def layout3():
    # in terms of formatting, the layout to the RIGHT of the = sign looks like a 2-line GUI (ignore the layout +=
    layout = [[sg.Button(i) for i in range(4)]]
    # this row is better than, but is the same as
    layout += [[sg.OK()]]
    # .. this row in that they both add a new ROW with a button on it
    layout.append([sg.Cancel()])

    window = sg.Window('Generated Layouts', layout)

    event, values = window.read()

    print(event, values)
    window.close()


"""
    Construct 4 - Using + to place Elements on the same row
    
    If you want to put elements on the same row, you can simply add them together.  All that is happening is that the
    items in one list are added to the items in another.  That's true for all these contructs using +
"""


def layout4():
    layout = [[sg.Text('Enter some info')] + [sg.Input()] + [sg.Exit()]]

    window = sg.Window('Generated Layouts', layout)

    event, values = window.read()

    print(event, values)
    window.close()


"""
    Construct #5 - Simple "concatenation" of layouts
    Layouts are lists of lists.  Some of the examples and demo programs use a .append method to add rows to layouts.
    These will soono be replaced with this new technique.  It's so simple that I don't know why it took so long to
    find it.
    This layout uses list comprehensions heavily, and even uses 2 of them. So, if you find them confusing, skip down
    to the next Construct and you'll see the same layout built except for loops are used rather than comprehensions
    
    The next 3 examples all use this same window that is layed out like this:
        Each row is:
    Text1, Text2, Radio1, Radio2, Radio3, Radio4, Radio5
    Text1, Text2, Radio1, Radio2, Radio3, Radio4, Radio5
    ...
    
    It shows, in particular, this handy bit of layout building, a += to add on additional rows.
    layout =  [[stuff on row 1], [stuff on row 2]]
    layout += [[stuff on row 3]]
    
    Works as long as the things you are adding together look like this [[ ]]  (the famous double bracket layouts of PSG)
"""


def layout5():
    questions = ('Managing your day-to-day life', 'Coping with problems in your life?', 'Concentrating?',
                 'Get along with people in your family?', 'Get along with people outside your family?',
                 'Get along well in social situations?', 'Feel close to another person',
                 'Feel like you had someone to turn to if you needed help?', 'Felt confident in yourself?')

    layout = [[sg.Text(qnum + 1, size=(2, 2)), sg.Text(q, size=(30, 2))] +
              [sg.Radio('', group_id=qnum, size=(7, 2),
                        key=(qnum, col)) for col in range(5)]
              for qnum, q in enumerate(questions)]
    layout += [[sg.OK()]]

    window = sg.Window('Computed Layout Questionnaire', layout)
    event, values = window.read()

    print(event, values)
    window.close()


"""
    Construct #6 - Computed layout without using list comprehensions
    This layout is identical to Contruct #5.  The difference is that rather than use list comprehensions, this code
    uses for loops.  Perhaps if you're a beginner this version makes more sense?

    In this example we start with a "blank layout" [[ ]] and add onto it.

    Works as long as the things you are adding together look like this [[ ]]  (the famous double bracket layouts of PSG)
"""


def layout6():
    questions = ('Managing your day-to-day life', 'Coping with problems in your life?', 'Concentrating?',
                 'Get along with people in your family?', 'Get along with people outside your family?',
                 'Get along well in social situations?', 'Feel close to another person',
                 'Feel like you had someone to turn to if you needed help?', 'Felt confident in yourself?')

    layout = [[]]
    for qnum, question in enumerate(questions):
        # rows start with # and question
        row_layout = [sg.Text(qnum + 1, size=(2, 2)),
                      sg.Text(question, size=(30, 2))]

        # loop through 5 radio buttons and add to row
        for radio_num in range(5):
            row_layout += [sg.Radio('', group_id=qnum,
                                    size=(7, 2), key=(qnum, radio_num))]
        # after row is completed layout, tack it onto the end of final layout
        layout += [row_layout]

    # and finally, add a row to the bottom that has an OK button
    layout += [[sg.OK()]]

    window = sg.Window('Computed Layout Questionnaire', layout)
    event, values = window.read()

    print(event, values)
    window.close()


"""
    Construct #7 - * operator and list comprehensions 
        Using the * operator from inside the layout
        List comprehension inside the layout
        Addition of rows to layouts
        All in a single variable assignment
        
    NOTE - this particular code, using the * operator, will not work on Python 2 and think it was added in Python 3.5
    
    This code shows a bunch of questions with Radio Button choices
    
    There is a double-loop comprehension used.  One that loops through the questions (rows) and the other loops through
    the Radio Button choices.
    Thus each row is:
    Text1, Text2, Radio1, Radio2, Radio3, Radio4, Radio5
    Text1, Text2, Radio1, Radio2, Radio3, Radio4, Radio5
    Text1, Text2, Radio1, Radio2, Radio3, Radio4, Radio5
    
    What the * operator is doing in these cases is expanding the list they are in front of into a SERIES of items
    from the list... one after another, as if they are separated with comma.  It's a way of "unpacking" from within
    a statement.
    
    The result is a beautifully compact way to make a layout, still using a layout variable, that consists of a
    variable number of rows and a variable number of columns in each row.
"""


def layout7():
    questions = ('Managing your day-to-day life', 'Coping with problems in your life?', 'Concentrating?',
                 'Get along with people in your family?', 'Get along with people outside your family?',
                 'Get along well in social situations?', 'Feel close to another person',
                 'Feel like you had someone to turn to if you needed help?', 'Felt confident in yourself?')

    # These are the question # and the question text
    layout = [[*[sg.Text(qnum + 1, size=(2, 2)), sg.Text(q, size=(30, 2))],
               # finally add an OK button at the very bottom by using the '+' operator
               *[sg.Radio('', group_id=qnum, size=(7, 2), key=(qnum, col)) for col in range(5)]] for qnum, q in enumerate(questions)] + [[sg.OK()]]

    window = sg.Window('Questionnaire', layout)

    event, values = window.read()

    print(event, values)
    window.close()


"""
    Construct #8 - Computed layout using list comprehension and concatenation
    This layout shows one practical use, a multiple choice test.  It's been left parse as to focus on the generation
    part of the program.  For example, default keys are used on the Radio elements.  In reality you would likely
    use a tuple of the question number and the answer number.

    In this example we start with a "Header" Text element and build from there.
"""


def layout8():
    # The questions and answers
    q_and_a = [
        ['1. What is the thing that makes light in our solar system',
            ['A. The Moon', 'B. Jupiter', 'C. I dunno']],
        ['2. What is Pluto', ['A. The 9th planet', 'B. A dwarf-planet',
                              'C. The 8th planet', 'D. Goofies pet dog']],
        ['3. When did man step foot on the moon', ['A. 1969', 'B. 1960', 'C. 1970', 'D. 1869']], ]

    # make Header larger
    layout = [[sg.Text('Astronomy Quiz #1', font='ANY 15', size=(30, 2))]]

    # "generate" the layout for the window based on the Question and Answer information
    for qa in q_and_a:
        q = qa[0]
        a_list = qa[1]
        layout += [[sg.Text(q)]] + [[sg.Radio(a, group_id=q)]
                                 for a in a_list] + [[sg.Text('_' * 50)]]

    layout += [[sg.Button('Submit Answers', key='SUBMIT')]]

    window = sg.Window('Multiple Choice Test', layout)

    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'SUBMIT'):
            break
    sg.popup('The answers submitted were', values)
    window.close()


# ------------------------- Call each of the Constructs -------------------------

layout0()
# layout1()
# layout2()
# layout3()
# layout4()
# layout5()
# layout6()
# layout7()
# layout8()
