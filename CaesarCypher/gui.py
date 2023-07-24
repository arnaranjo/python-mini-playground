'''
CLASS AppGUI:
    Set the GUI of the application.
'''

import tkinter as tk
from tkinter import messagebox

class AppGUI(tk.Tk):
    def __init__(self, Controller):
        super().__init__()

        self.controller = Controller

        self.title("Caesar Cypher")
        self.resizable(0,0)
            # .resizable(0,0) Restricts the root window to change.

        self.FONT_FAMILY = "arial"
        self.FONT_SIZE = 11
        self.FONT_TYPE = "normal"

        self.varRadio = tk.IntVar()
        self.varStep = tk.IntVar()

        # MENU BAR --------------------------------------------------------------#

        menuBar = tk.Menu(self)
        self.config(menu = menuBar)

        menuView = tk.Menu(menuBar, tearoff = "off")
        menuBar.add_cascade(label = "View", menu=menuView)
        menuHelp = tk.Menu(menuBar, tearoff = "off")
        menuBar.add_cascade(label = "Help", menu = menuHelp)
            # tearoff allows you to detach menus for the main window creating floating menus.

        menuView.add_command(
            label = "Clean entry",
            command = self.opClear,
            font = (self.FONT_FAMILY, self.FONT_SIZE, self.FONT_TYPE)
        )
        menuView.add_command(
            label = "Exit",
            command = self.opExit,
            font = (self.FONT_FAMILY, self.FONT_SIZE, self.FONT_TYPE)
        )

        menuHelp.add_command(
            label = "About...",
            command = self.opAbout,
            font = (self.FONT_FAMILY, self.FONT_SIZE, self.FONT_TYPE)
        )

        # WIDGETS ---------------------------------------------------------------#

        mainLabel = tk.Label(
            text = "Wellcome to CCypher.",
            borderwidth = 1,
            relief = "solid",
            font = (self.FONT_FAMILY, self.FONT_SIZE + 2, self.FONT_TYPE)
        ).grid(column=0, row=0, padx=10, pady=20, columnspan=2, sticky='ew')
            # sticky -- specifies a value of S , N , E , W , or a combination of them, e.g. NW , NE , SW , or SE. 
            # The parameter tells which side of the "cell" the widget will "stick" to.        
        
        textLabel = tk.Label(
            text = "Type a text:",
            font = (self.FONT_FAMILY, self.FONT_SIZE, self.FONT_TYPE)
        ).grid(column=0, row=1, padx=10, pady=5, sticky='ew')

        stepLabel = tk.Label(
            text = "Select the step:",
            font = (self.FONT_FAMILY, self.FONT_SIZE, self.FONT_TYPE)
        ).grid(column=0, row=2, padx=10, pady=5, sticky='ew')

        resultTextLabel = tk.Label(
            text = "Result:",
            font = (self.FONT_FAMILY, self.FONT_SIZE, self.FONT_TYPE)
        ).grid(column=0, row=7, padx=10, pady=5, sticky='ew')

        self.textEntry = tk.Entry(self,
            font = (self.FONT_FAMILY, self.FONT_SIZE, self.FONT_TYPE)
        )
        self.textEntry.grid(column=1, row=1, padx=10, pady=5, sticky='ew')

        self.numberStep = tk.Spinbox(
            from_= 1,
            to = 20,
            textvariable = self.varStep,
            font = (self.FONT_FAMILY, self.FONT_SIZE, self.FONT_TYPE)
        )
        self.numberStep.grid(column=1, row=2, padx=10, pady=5, sticky='ew')

        self.exeCipher = tk.Button(
            text = "Execute",
            command = self.controller.Execute,
            font = (self.FONT_FAMILY, self.FONT_SIZE, self.FONT_TYPE)
        )
        self.exeCipher.grid(column=0, row=3, padx=10, pady=5, sticky='ew')  

        self.copyText = tk.Button(
            text = "Copy result",
            command = self.CopyResult,
            font = (self.FONT_FAMILY, self.FONT_SIZE, self.FONT_TYPE)
        )
        self.copyText.grid(column=0, row=4, padx=10, pady=5, sticky='ew')

        self.rButtonA = tk.Radiobutton(
            text = "Encrypt text.",
            variable=self.varRadio,
            value = 0,
            font = (self.FONT_FAMILY, self.FONT_SIZE, self.FONT_TYPE)
        ).grid(column=0, row=5, padx=10, pady=0, sticky='w')

        self.rButtonB = tk.Radiobutton(
            text = "Dencryp text.",
            variable=self.varRadio,
            value = 1,
            font = (self.FONT_FAMILY, self.FONT_SIZE, self.FONT_TYPE)
        )
        self.rButtonB.grid(column=0, row=6, padx=10, pady=0, sticky='w') 

        self.resultLabel = tk.Label(
            borderwidth = 1,
            relief = "solid",
            font = (self.FONT_FAMILY, self.FONT_SIZE + 2, self.FONT_TYPE)
        )
        self.resultLabel.grid(column=1, row=7, padx=10, pady=15, sticky='ew')

        # METHODS ---------------------------------------------------------------#

    def opClear(self):
        self.textEntry.delete(0, tk.END)
        self.resultLabel.config(text = "Result.")

    def CopyResult(self):
        self.clipboard_clear
        self.clipboard_append(self.resultLabel.cget("text"))
            # .cget(option) This method returns the value for the specified option.

    def opExit(self):
        self.quit()

    def textError(self):
        messagebox.showinfo(title = "Error",message = "The text input is invalid.")

    def opAbout(self):
        messagebox.showinfo(
            title = "About",
            message = 
'''Welcome to my Python text encryption and decryption app Have fun exploring and experimenting with the code!\n
https://github.com/arnaranjo/python-mini-playground'''
        )