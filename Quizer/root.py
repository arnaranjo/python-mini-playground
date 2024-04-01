import base64
import customtkinter as ctk
import config as cf
from random import choice
from home import HomeGUI
from settings import SettingsGUI
from quiz_multiple import MultipleQuizGUI
from quiz_boolean import BooleanQuizGUI
from quiz_results import ResultsGUI


class RootGUI(ctk.CTk):
    def __init__(self, Controller):
        super().__init__()
        
        self.controller = Controller
        self.currentFrame = None

        # Variables setted in main.
        self.categoryNamesList = []
        self.categoryData = []

        self.questions = []
        self.answerSelectedList = []
        self.apiParameters = {}

        self.title("Quizer")
        self.geometry(f"{cf.WINDOW_WIDTH}x{cf.WINDOW_HEIGHT}")
        self.resizable(False,False)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Set the main screen.
        self.SwitchHome()


    def SwitchSettings(self):
        if self.currentFrame is not None:
            self.currentFrame.destroy()
        self.currentFrame = SettingsGUI(master = self)

        self.currentFrame.categoryBox.configure(values= self.categoryNamesList)
        self.currentFrame.saveButton.configure(command= self.SaveSettings)
        self.currentFrame.homeButton.configure(command= self.SwitchHome)

        self.currentFrame.grid(row=0, column=0, sticky="nsew")


    def SwitchHome(self):
        if self.currentFrame is not None:
            self.currentFrame.destroy()
        self.currentFrame = HomeGUI(master= self)

        self.currentFrame.settingsButton.configure(command= self.SwitchSettings)
        self.currentFrame.startButton.configure(command= lambda : self.ShowQuiz(0))
        self.currentFrame.quitButton.configure(command = self.quit)

        self.currentFrame.grid(row=0, column=0, sticky="nsew")

        if not self.apiParameters:
            self.currentFrame.startButton.configure(state= "disabled")
        else:
            self.currentFrame.startButton.configure(state= "normal")


    def SwitchBoolean(self):
        if self.currentFrame is not None:
            self.currentFrame.destroy()
        self.currentFrame = BooleanQuizGUI(master= self)

        self.currentFrame.homeButton.configure(command= self.SwitchHome)
        self.currentFrame.buttonTrue.configure(command= lambda : self.CheckBoolAnswer("True"))
        self.currentFrame.buttonFalse.configure(command= lambda : self.CheckBoolAnswer("False"))

        self.currentFrame.grid(row=0, column=0, sticky="nsew")

        self.ResetParameters()


    def SwitchMultipleQuiz(self):
        if self.currentFrame is not None:
            self.currentFrame.destroy()
        self.currentFrame = MultipleQuizGUI(master= self)

        self.currentFrame.homeButton.configure(command= self.SwitchHome)
        self.currentFrame.buttonA.configure(command= lambda : self.CheckMultiAnswer(0))
        self.currentFrame.buttonB.configure(command= lambda : self.CheckMultiAnswer(1))
        self.currentFrame.buttonC.configure(command= lambda : self.CheckMultiAnswer(2))
        self.currentFrame.buttonD.configure(command= lambda : self.CheckMultiAnswer(3))

        self.currentFrame.grid(row=0, column=0, sticky="nsew")

        self.ResetParameters()


    def SwitchResuls(self, corrects, total):
        if self.currentFrame is not None:
            self.currentFrame.destroy()
        self.currentFrame = ResultsGUI(master= self)

        self.currentFrame.homeButton.configure(command= self.SwitchHome)
        self.currentFrame.resultLabel.configure(text= f"{corrects} / {total}")

        self.currentFrame.grid(row=0, column=0, sticky="nsew")

        # Empty the parameters to reset the quiz.
        self.apiParameters = {}
    

    def SaveSettings(self):
        self.apiParameters = {}
        self.apiParameters = self.currentFrame.GetSelections(self.categoryData)

        print(self.apiParameters) #<-------------- TEST.

        # Request the questions with the parameters selected.
        self.controller.RequestQuestions(self.apiParameters)
        
    # Show the quiz in the window, It depens on the type of quiz.
    def ShowQuiz(self, num):
        self.questions = self.controller.questionsRequested[num]

        #Conversion from base64 encode to string.
        type = base64.b64decode(self.questions["type"]).decode("utf-8")

        if type == "multiple":
            self.SwitchMultipleQuiz()
            self.ShowQuestion()       
            AnswerList = self.GetAnsweres()
            self.SetText(AnswerList)   

        elif type == "boolean":
            self.SwitchBoolean()
            self.ShowQuestion()

    # Set the text of the TextArea
    def ShowQuestion(self):
        self.currentFrame.textQuiz.delete("0.0", "end")
        self.currentFrame.textQuiz.insert(
            "0.0",
            base64.b64decode(self.questions["question"]).decode("utf-8")                
        )
    
    # Set the text of the buttons randomly from the list of results.
    # Only is used for multiple quiz.
    def SetText(self, list):        
        self.answerSelectedList = []

        for button in self.currentFrame.buttonList:
            answerSelected = choice(list)
            button.configure(
                text = answerSelected
            )
            list.pop(list.index(answerSelected))
            self.answerSelectedList.append(answerSelected)
        print(self.answerSelectedList) #<-------------- TEST.
    
    # Return a list of results for multiple and boolean quiz.
    def GetAnsweres(self):
        resultList = []

        resultList.append(base64.b64decode(self.questions["correct_answer"]).decode("utf-8"))
        for answer in self.questions["incorrect_answers"]:
            resultList.append(base64.b64decode(answer).decode("utf-8"))

        print(resultList)
        return resultList

    # Number: 
    # 0 (Text of Button A)
    # 1 (Text of Button B)
    # 2 (Text of Button C)
    # 3 (Text of Button D)
    def CheckMultiAnswer(self, number):
        self.controller.BeginQuiz(self.answerSelectedList[number])


    def CheckBoolAnswer(self, answer):
        self.controller.BeginQuiz(answer)

    # Only when the player returns to the home windows, are the parameters reset.
    def ResetParameters(self):
        self.apiParameters = {}