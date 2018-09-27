# TCC
#20/1/18  Oz date

from tkinter import *

def callback(event):            #used to allow Return key as well as
    calculate()                 # button press for mark entry


def calculate():
    global i, total,name
    name = entry_name.get()         #get the name and prevent another
    mark[i] = entry_mark.get()
    label_name.configure(state = DISABLED)
    entry_name.configure(state = DISABLED)
    mark[i] = entry_mark.get()      #get and store in mark list and clear entry
    entry_mark.delete(0,END)
    i = i + 1                       #get total i - needs to be global
    if i == 4:                      #if four marks - stop
        button_done.configure(state = NORMAL)
        button_calculate.configure(state = DISABLED)
        
def done():
    total = 0
    for m in mark:                  #total marks - convery to integer
        total += int(m)
    average = total/4               #calculate average
    f = open(pathname, 'w')
    print(name, file= f)
    print(total, file= f)           #write to file
    print(average, file= f)
    f.close()
    button_done.configure(state = DISABLED)     #stop button being pressed again
    button_display.configure(state = NORMAL)
    

def display():
    #create list of three valuesand combine elemnets into one string - use \n for new line
    data = [line.strip() for line in open(pathname)]
    s= 'Name: ' + data[0] +'\nTotal: ' + str(data[1]) + '\nAverage: ' + str(data[2])
    label_displayresults.configure(text = s)


root = Tk()
root.title('text files')

#set up controls
label_instructs = Label(justify = LEFT, padx = 10, pady=10,width = 30, height =4, text = 'Enter a Name then a Mark then press\nCalculate, do this 4 times.Then press\nDone to Save Name, Total and Average.')   
label_name = Label(text='Name: ', width = 8)
entry_name = Entry(width = 8)
label_mark = Label(text='Mark: ', width = 8)
entry_mark = Entry(width = 8)
button_calculate = Button(text = 'Calculate', command=calculate)
button_done= Button(pady = 8, text='Done', command = done, state = DISABLED)
button_display = Button(pady =8,text = 'Display', command=display, state = DISABLED)
label_displaytext = Label(justify = LEFT, text='Press display to\nretrieve recent\nTotal & Average')
label_displayresults=Label(justify = LEFT, padx = 10, height = 5,)
                           
#set up positioning of controls
label_instructs.grid(row = 0, columnspan = 3)
label_name.grid(row = 1, column = 0)
entry_name.grid(row = 1, column = 1)
label_mark.grid(row = 2, column = 0)
entry_mark.grid(row = 2, column = 1)

entry_mark.bind('<Return>', callback)       #create binding for Return key for mark entry box

button_calculate.grid(row =3, column = 0)
button_done.grid(row = 3, column = 1)
button_display.grid(row = 4, column = 0)
label_displaytext.grid(row = 4, column = 1)
label_displayresults.grid(row = 5, columnspan = 2)

#global variables when used in more than one function
global i
global mark
global total
global average
i=total=0
mark = [0,0,0,0]
average = 0.0
entry_name.focus()          #set initial focus

global pathname

pathname = "C:\\Users\\tcrewe\\Dropbox\\01 Teaching folders\\07 TCC Python stuff\\TCC py files\\TCC sample files\wordlist.txt"

mainloop()
