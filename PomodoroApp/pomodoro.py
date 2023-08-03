'''
    class PomodoroModel
'''

from math import floor

class PomodoroModel:
    def __init__(self):
        
        self.workTime = 25 * 60
        self.shortBreak = 5 * 60
        self.longBreak = 15 * 60
        
        self.count = 0
    
    def TimeFormat(self, second):
        secondFormat = second % 60
        minuteFormat = floor(second / 60)

        if minuteFormat < 10:
            minuteFormat = f"0{minuteFormat}"
        if secondFormat < 10:
            secondFormat = f"0{secondFormat}"
        elif secondFormat == 0:
            secondFormat = "00"

        return f"{minuteFormat}:{secondFormat}"