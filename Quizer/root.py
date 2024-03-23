'''
Custom tkinter Documentation: https://customtkinter.tomschimansky.com/documentation/
    Creator: https://github.com/TomSchimansky
Color palette: https://coolors.co/palette/355070-6d597a-b56576-e56b6f-eaac8b
'''


from random import choice
import base64
import customtkinter as ctk
from home import HomeGUI
from settings import SettingsGUI
from quiz_multiple import MultipleQuizGUI
from quiz_boolean import BooleanQuizGUI

WINDOW_WIDTH = 450
WINDOW_HEIGHT = 500
FONT_FAMILY = "arial"
FONT_SIZE = 11
FONT_TYPE = "normal"


class RootGUI(ctk.CTk):
    def __init__(self, Controller):
        super().__init__()
        
        self.controller = Controller
        self.currentFrame = None

        self.categoryNamesList = []
        self.categoryData = []
        self.questions = []
        self.answerSelectedList = []

        self.apiParameters = {
            "amount": 10
        }

        self.title("Quizer")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.resizable(False,False)


        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Set the main screnn:
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
        
        self.currentFrame.grid(row=0, column=0, sticky="nsew")


    def SwitchBoolean(self):
        if self.currentFrame is not None:
            self.currentFrame.destroy()
        self.currentFrame = BooleanQuizGUI(master= self)

        self.currentFrame.homeButton.configure(command= self.SwitchHome)

        self.currentFrame.grid(row=0, column=0, sticky="nsew")


    def SwitchMultipleQuiz(self):
        if self.currentFrame is not None:
            self.currentFrame.destroy()
        self.currentFrame = MultipleQuizGUI(master= self)

        self.currentFrame.homeButton.configure(command= self.SwitchHome)
        self.currentFrame.buttonA.configure(command= lambda : self.CheckAnswer(0))
        self.currentFrame.buttonB.configure(command= lambda : self.CheckAnswer(1))
        self.currentFrame.buttonC.configure(command= lambda : self.CheckAnswer(2))
        self.currentFrame.buttonD.configure(command= lambda : self.CheckAnswer(3))

        self.currentFrame.grid(row=0, column=0, sticky="nsew")


    def SearchCategoryID(self):
        if self.currentFrame.categoryBox.get() != "Any Category":
            for category in self.categoryData:
                if category["name"] == self.currentFrame.categoryBox.get():
                    self.apiParameters["category"] = category["id"]
        elif self.currentFrame.categoryBox.get() == "Any Category" \
            and "category" in self.apiParameters:
            self.apiParameters.pop("category")

    #TODO Change this function to settings.py an
    def SaveSettings(self):
        self.apiParameters["amount"] = int(self.currentFrame.numberSelector.get())
        self.SearchCategoryID()

        if self.currentFrame.difficultyBox.get() != "Any Difficulty":
            if self.currentFrame.difficultyBox.get() == "Easy":
                self.apiParameters["difficulty"] = "easy"
            elif self.currentFrame.difficultyBox.get() == "Medium":
                self.apiParameters["difficulty"] = "medium"
            elif self.currentFrame.difficultyBox.get() == "Hard":
                self.apiParameters["difficulty"] = "hard"
        elif self.currentFrame.difficultyBox.get() == "Any Difficulty" \
            and "difficulty" in self.apiParameters:
            self.apiParameters.pop("difficulty")

        if self.currentFrame.typeBox.get() != "Any Type":
            if self.currentFrame.typeBox.get() == "Multiple":
                self.apiParameters["type"] = "multiple"
            elif self.currentFrame.typeBox.get() == "True/False":
                self.apiParameters["type"] = "boolean"
        elif self.currentFrame.typeBox.get() == "Any Type" \
            and "type" in self.apiParameters:
            self.apiParameters.pop("type")

        # Request the parameters
        self.controller.RequestQuestions(self.apiParameters)
        

    # Show the quiz in the window
    def ShowQuiz(self, num):
        self.questions = self.controller.questionsRequested[num]

        #Conversion from base64 encode to string.
        type = base64.b64decode(self.questions["type"]).decode("utf-8")

        AnswerList = []
        if type == "multiple":
            self.SwitchMultipleQuiz()
            self.ShowQuestion()       
            AnswerList = self.GetAnsweres()
            self.SetText(AnswerList)   

        elif type == "boolean":
            self.SwitchBoolean()
            self.ShowQuestion()
            AnswerList = self.GetAnsweres()

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

        print(list) #<-------------- TEST.
        self.answerSelectedList = []

        for button in self.currentFrame.buttonList:
            answerSelected = choice(list)
            button.configure(
                text = answerSelected
            )
            list.pop(list.index(answerSelected))
            self.answerSelectedList.append(answerSelected)
        print(self.answerSelectedList)
    
    # Return a list of results for multiple and boolean quiz.
    def GetAnsweres(self):
        resultList = []

        resultList.append(base64.b64decode(self.questions["correct_answer"]).decode("utf-8"))
        for answer in self.questions["incorrect_answers"]:
            resultList.append(base64.b64decode(answer).decode("utf-8"))

        return resultList

    # 
    def CheckAnswer(self, number):

        print(self.answerSelectedList[number]) #<-------------- TEST.
        
        self.controller.BeginQuiz(self.answerSelectedList[number])

