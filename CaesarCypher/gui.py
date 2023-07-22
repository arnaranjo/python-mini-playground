import tkinter as tk

class AppGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Caesar Cypher")
        self.resizable(0,0)

        self.FONT_FAMILY = "arial"
        self.FONT_SIZE = 11
        self.FONT_TYPE = "normal"

        self.varRadio = tk.IntVar()

        self.mainLabel = tk.Label(
            text = "Wellcome to CCypher.",
            borderwidth = 1,
            relief = "solid",
            font = (self.FONT_FAMILY,self.FONT_SIZE + 2,self.FONT_TYPE)
        ).grid(column=0, row=0, padx=10, pady=20, columnspan=2, sticky='ew')        
        
        self.textLabel = tk.Label(
            text = "Type a text:",
            borderwidth = 1,
            relief = "solid",
            font = (self.FONT_FAMILY,self.FONT_SIZE,self.FONT_TYPE)
        ).grid(column=0, row=1, padx=10, pady=5, sticky='ew')

        self.textEntry = tk.Entry(
            font = (self.FONT_FAMILY,self.FONT_SIZE,self.FONT_TYPE)
        ).grid(column=1, row=1, padx=10, pady=5, sticky='ew')

        self.exeCipher = tk.Button(
            text = "Execute",
            font = (self.FONT_FAMILY,self.FONT_SIZE,self.FONT_TYPE)
        ).grid(column=0, row=2, padx=10, pady=5, sticky='ew')  

        self.rButtonA = tk.Radiobutton(
            text = "Encrypt text.",
            variable=self.varRadio,
            value = 0,
            font = (self.FONT_FAMILY,self.FONT_SIZE,self.FONT_TYPE)
        ).grid(column=0, row=3, padx=10, pady=0, sticky='w')

        self.rButtonB = tk.Radiobutton(
            text = "Dencryp text.",
            variable=self.varRadio,
            value = 1,
            font = (self.FONT_FAMILY,self.FONT_SIZE,self.FONT_TYPE)
        ).grid(column=0, row=4, padx=10, pady=0, sticky='w') 

        self.resultLabel = tk.Label(
            text = "Result",
            borderwidth = 1,
            relief = "solid",
            font = (self.FONT_FAMILY,self.FONT_SIZE + 2,self.FONT_TYPE)
        ).grid(column=0, row=5, padx=10, pady=15, columnspan=2, sticky='ew')      

        tk.mainloop()


