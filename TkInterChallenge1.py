try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

# list(list(tuple()))
keys = [[('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 1), ('/', 1)],
        ]

mainWindowPadding = 8

mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = mainWindowPadding

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='nsew')

keypad = tkinter.Frame(mainWindow)
keypad.grid(row=0, column=0, sticky='nsew')

row = 0
for keyRow in keys:
    col = 0
    for key in keyRow:
        tkinter.Button(keypad, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        #print(key[0])
        #print(key[1])
        col = col + key[1]
        #print("next column is " , col)
        #print("=" * 5)
    row = row + 1
    #print("next row is " ,row)
    #print("=" * 20)


mainWindow.mainloop()

