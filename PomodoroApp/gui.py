import tkinter as tk


class PomodoroGUI(tk.Tk):
    def __init__(self, Controller):
        super().__init__()

        self.title("Pomodoro App")
        self.geometry("250x100")