from pomodoro import PomodoroModel
from gui import PomodoroGUI


class PomodoroController:
    def __init__(self, Model, View):

        self.model = Model
        self.view = View

if __name__ == "__main__":

    newPomodoroModel = PomodoroModel()
    newPomodoroControl = PomodoroController(newPomodoroModel, None)
    newPomodoroGUI = PomodoroGUI(newPomodoroControl)
    newPomodoroControl.view = newPomodoroGUI
    newPomodoroGUI.mainloop()