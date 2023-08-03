'''
    class PomodoroController
'''

from pomodoro import PomodoroModel
from gui import PomodoroGUI

class PomodoroController:
    def __init__(self, Model, View):

        self.model = Model
        self.view = View
    
    def StartTimer(self):
        self.view.timeLabel.config(text="10:10")
        self.view.workLabel.config(text="Working...")
    
    def ResetTimer(self):
        self.view.timeLabel.config(text="TIME")
        self.view.workLabel.config(text="Let's Work!")

if __name__ == "__main__":

    newPomodoroModel = PomodoroModel()
    newPomodoroControl = PomodoroController(newPomodoroModel, None)
    newPomodoroGUI = PomodoroGUI(newPomodoroControl)
    newPomodoroControl.view = newPomodoroGUI
    newPomodoroGUI.mainloop()