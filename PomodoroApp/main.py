from pomodoro import PomodoroModel
from gui import PomodoroGUI

class PomodoroController:
    def __init__(self, Model: PomodoroModel, View: PomodoroGUI):

        self.model = Model
        self.view = View
        self.currentTime = None

        self.count = 0

    def StartTimer(self):
        self.count += 1
        if self.count % 8 == 0:
            self.currentTime = self.model.longBreak
            self.view.workLabel.config(text = "Break time!")
            self.view.FixIMG()
            self.CountDown(self.currentTime)

        elif self.count % 2 == 0:
            self.currentTime = self.model.shortBreak
            self.view.workLabel.config(text = "Short break!")
            self.view.FixIMG()
            self.CountDown(self.currentTime)

        else:
            self.currentTime = self.model.workTime
            self.view.workLabel.config(text = "Working...")
            self.view.RotateIMG()
            self.CountDown(self.currentTime)
        
    def CountDown(self, timeLeft):
        self.view.timeLabel.config(
            text = self.model.TimeFormat(timeLeft)
        )

        if timeLeft == 0:
            self.StartTimer()
        else:             
            self.view.Timer()

    def ResetTimer(self):
        self.count = 0
        self.view.timeLabel.config(text = "TIME")
        self.view.workLabel.config(text = "Let's Work!")

if __name__ == "__main__":

    newPomodoroModel = PomodoroModel()
    newPomodoroControl = PomodoroController(newPomodoroModel, None)
    newPomodoroGUI = PomodoroGUI(newPomodoroControl)
    newPomodoroControl.view = newPomodoroGUI
    newPomodoroGUI.mainloop()