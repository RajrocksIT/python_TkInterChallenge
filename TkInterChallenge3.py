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
        col = col + key[1]

    row = row + 1


# Below things will stop from hiding the buttons when we try to resize
mainWindow.update()
mainWindow.minsize(keypad.winfo_width() + mainWindowPadding, result.winfo_height() + keypad.winfo_height())
mainWindow.maxsize(keypad.winfo_width() + 50 + mainWindowPadding, result.winfo_height() + 50 + keypad.winfo_height())
# Now the calculator will open with perfect size. like a real calculator. but we can strech upto 50 max and 50 min.

mainWindow.mainloop()

