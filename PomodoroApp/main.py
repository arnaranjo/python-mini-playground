'''
    class PomodoroController
'''

from pomodoro import PomodoroModel
from gui import PomodoroGUI

class PomodoroController:
    def __init__(self, Model: PomodoroModel, View: PomodoroGUI):

        self.model = Model
        self.view = View
        self.currentTime = None

    def StartTimer(self):
        self.model.count += 1
        print(self.model.count) #--------PRINT
        if self.model.count % 8 == 0:
            self.currentTime = self.model.longBreak
            self.CountDown(self.currentTime)

        elif self.model.count % 2 == 0:
            self.currentTime = self.model.shortBreak
            self.CountDown(self.currentTime)

        else:
            self.currentTime = self.model.workTime
            self.CountDown(self.currentTime)

        
    def CountDown(self, timeLeft):
        timeLeftFormated = self.model.TimeFormat(timeLeft)
        self.view.timeLabel.config(text = timeLeftFormated)

        if timeLeft == 0:
            self.StartTimer()
        else:             
            self.view.Timer()


    def ResetTimer(self):
        self.model.count = 0

if __name__ == "__main__":

    newPomodoroModel = PomodoroModel()
    newPomodoroControl = PomodoroController(newPomodoroModel, None)
    newPomodoroGUI = PomodoroGUI(newPomodoroControl)
    newPomodoroControl.view = newPomodoroGUI
    newPomodoroGUI.mainloop()