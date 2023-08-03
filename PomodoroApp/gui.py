'''
    class PomodoroGUI
Images Source:
https://www.flaticon.com/free-icon/pomodoro_7329721
https://www.flaticon.com/free-icon/play_3318660
https://www.flaticon.com/free-icon/restart_3106716
'''

import tkinter as tk

BACKGROUND_COLOR = "#22577a"
FONT_COLOR = "#d9dcd6"
FONT_NAME = "Courier"
POMODORO_IMG = "PomodoroApp/pomodoroIMG.png"
START_IMG = "PomodoroApp/startIMG.png"
RESET_IMG = "PomodoroApp/resetIMG.png"
WITH_BG = 350
HEIGHT_BG = 500


class PomodoroGUI(tk.Tk):
    def __init__(self, Controller):
        super().__init__()

        self.controller = Controller

        self.title("Pomodoro App")
        self.geometry(f"{WITH_BG}x{HEIGHT_BG}")
        self.resizable(False,False)
    
        self.pomodoroImage = tk.PhotoImage(file = POMODORO_IMG)
        self.startImage = tk.PhotoImage(file = START_IMG)
        self.resetImage = tk.PhotoImage(file = RESET_IMG)

        self.bgCanvas = tk.Canvas(            
            width = WITH_BG,
            height = HEIGHT_BG,
            background = BACKGROUND_COLOR
        )
        self.bgCanvas.pack()

        self.bgCanvas.create_image(175,200,image=self.pomodoroImage)

        self.buttonStart = tk.Button(
            image = self.startImage,
            command = self.StartBT
        )
        self.buttonStart.pack()
        self.buttonStart.place(relx = 0.3, y = 420)

        self.buttonReset = tk.Button(
            image = self.resetImage,
            command = self.ResetBT
        )
        self.buttonReset.pack()
        self.buttonReset.place(relx = 0.6, y = 420)

        self.workLabel = tk.Label(
            width = 10,
            text = "Let's Work!",
            fg = FONT_COLOR,
            background = BACKGROUND_COLOR,
            font = (FONT_NAME, 20, "normal")
        )
        self.workLabel.pack()
        self.workLabel.place(x = 100, y = 20)

        self.timeLabel = tk.Label(
            width = 10,
            text = "TIME",
            fg = FONT_COLOR,
            background = BACKGROUND_COLOR,
            font = (FONT_NAME, 30, "normal")
        )
        self.timeLabel.pack()
        self.timeLabel.place(x = 50, y = 350)

    def StartBT(self):
        self.controller.StartTimer()

    def ResetBT(self):
        self.controller.ResetTimer()