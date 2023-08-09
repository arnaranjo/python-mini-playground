'''
    class PomodoroGUI
        It sets the GUI and contains the methods to control the animation or buttons,
        as well as the timer delay.

PIL must be installed: pip install Pillow
Images Source:
https://www.flaticon.com/free-icon/pomodoro_7329721
https://www.flaticon.com/free-icon/play_3318660
https://www.flaticon.com/free-icon/restart_3106716
'''

from gc import disable, enable
import tkinter as tk
from PIL import Image, ImageTk
from math import sin, pi

BACKGROUND_COLOR = "#22577a"
FONT_COLOR = "#d9dcd6"
FONT_NAME = "Courier"
POMODORO_IMG = "PomodoroApp/pomodoroIMG.png"
START_IMG = "PomodoroApp/startIMG.png"
RESET_IMG = "PomodoroApp/resetIMG.png"
WITH_BG = 350
HEIGHT_BG = 500
MAX_ANGLE = 0.2
TIMER = None


class PomodoroGUI(tk.Tk):
    def __init__(self, Controller):
        super().__init__()

        self.controller = Controller

        self.title("Pomodoro App")
        self.geometry(f"{WITH_BG}x{HEIGHT_BG}")
        self.resizable(False,False)

        self.imgAngle: float = 0.0

        self.rotation = None

        # WIDGETS ---------------------------------------------------------------#

        self.pomodoroImagePIL = Image.open(POMODORO_IMG)
        self.pomodoroImage = ImageTk.PhotoImage(self.pomodoroImagePIL)
        self.startImage = tk.PhotoImage(file = START_IMG)
        self.resetImage = tk.PhotoImage(file = RESET_IMG)
        self.newRotatedCanvasIMG = None

        self.pomodoroCanvas = tk.Canvas(            
            width = WITH_BG,
            height = HEIGHT_BG,
            background = BACKGROUND_COLOR
        )
        self.pomodoroCanvas.pack()
        self.canvasIMG = self.pomodoroCanvas.create_image(
            (175, 200), 
            image = self.pomodoroImage
        )

        self.buttonStart = tk.Button(
            image = self.startImage,
            highlightthickness = 5,
            command = self.StartBT
        )
        self.buttonStart.pack()
        self.buttonStart.place(relx = 0.3, y = 420)

        self.buttonReset = tk.Button(
            image = self.resetImage,
            highlightthickness = 5,
            command = self.ResetBT,
            state = tk.DISABLED
        )
        self.buttonReset.pack()
        self.buttonReset.place(relx = 0.6, y = 420)

        self.workLabel = tk.Label(
            width = 15,
            text = "Let's Work!",
            fg = FONT_COLOR,
            background = BACKGROUND_COLOR,
            font = (FONT_NAME, 20, "normal")
        )
        self.workLabel.pack()
        self.workLabel.place(x = 60, y = 20)

        self.timeLabel = tk.Label(
            width = 10,
            text = "TIME",
            fg = FONT_COLOR,
            background = BACKGROUND_COLOR,
            font = (FONT_NAME, 30, "normal")
        )
        self.timeLabel.pack()
        self.timeLabel.place(x = 50, y = 350)

        # METHOBS ---------------------------------------------------------------#

    def StartBT(self):
        self.buttonStart.config(state = tk.DISABLED)
        self.buttonReset.config(state = tk.NORMAL)
        self.controller.StartTimer()

    def ResetBT(self):
        self.buttonStart.config(state = tk.NORMAL)
        self.buttonReset.config(state = tk.DISABLED)
        self.controller.ResetTimer()
        self.FixIMG()
        self.CancelTimer()

    def SetIMG(self, newIMG):
        self.newRotatedCanvasIMG = ImageTk.PhotoImage(newIMG)

        self.pomodoroCanvas.itemconfig(
            self.canvasIMG,
            image = self.newRotatedCanvasIMG
        ) 

    def FixIMG(self):
        self.after_cancel(self.rotation)
        self.imgAngle = 0.0
        fixIMG = self.pomodoroImagePIL.rotate(0)
        self.SetIMG(fixIMG)

    def RotateIMG(self):
        self.imgAngle += 0.04
        
        rotatedIMG = self.pomodoroImagePIL.rotate(
            angle =  ((MAX_ANGLE - sin(self.imgAngle) * MAX_ANGLE * 180)/pi),
            expand = True,
            resample = Image.BICUBIC
        )

        self.SetIMG(rotatedIMG)       
            
        self.rotation = self.after(
            ms = 10,
            func = self.RotateIMG
        )

    def Timer(self):
        global TIMER
        self.controller.currentTime -= 1
        TIMER = self.after(
            ms = 1000,
            func = lambda: self.controller.CountDown(self.controller.currentTime)
        )
        
    def CancelTimer(self):
        self.after_cancel(TIMER)