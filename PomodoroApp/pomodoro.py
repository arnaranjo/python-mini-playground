'''
    class PomodoroModel
        This class contains only the pomodoro settings,
        additionally it has a method to format the time.
'''

from math import floor

WORK_TIME = 25 * 60
SHORT_BREAK = 5 * 60 
LONG_BREAK = 15 * 60

class PomodoroModel:
    def __init__(self):
                
        self.workTime = WORK_TIME
        self.shortBreak = SHORT_BREAK
        self.longBreak = LONG_BREAK
            
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