import base64
import config as cf
from random import choice
from root import RootGUI
from quizer import QuizerModel


class QuizerController():
    def __init__(self, View: RootGUI, Model :QuizerModel): 
        self.view = View
        self.model = Model
        self.quizNumber = 0
        self.rightAnswers = 0
        self.questionsRequested = []
        

    def RequestQuestions(self, parameters):
        self.model.finalParameters = parameters
        self.questionsRequested = self.model.LookUpQuestions()


    def BeginQuiz(self, answer):        
        quote = ""

        correctAnswer = base64.b64decode(
            self.questionsRequested[self.quizNumber]["correct_answer"]
        ).decode("utf-8")

        if answer == correctAnswer: 
            print("OK")
            self.rightAnswers += 1         
        else:
            print("FAIL")

        self.quizNumber += 1 
                   
        if self.quizNumber >= len(self.questionsRequested):          
            if self.rightAnswers >= (self.quizNumber/2):
                quote = choice(cf.TEX_GOOD_RESULT)

            if self.rightAnswers == self.quizNumber:
                quote = choice(cf.TEXT_EXCELENT_RESULT)
            
            if self.rightAnswers < (self.quizNumber/2):
                quote = choice(cf.TEXT_BAD_RESULT)

            self.view.SwitchResuls(
                self.rightAnswers,
                self.quizNumber,
                quote
            )
            self.quizNumber = 0
            self.rightAnswers = 0

        else:
            self.view.ShowQuiz(self.quizNumber)


if __name__ == "__main__":
    newModel = QuizerModel()
    newQuizer = QuizerController(None, newModel)
    newGUI = RootGUI(newQuizer)
    newQuizer.view = newGUI

    newQuizer.view.categoryData = newQuizer.model.LookUpCategoryData()
    newQuizer.view.categoryNamesList = newQuizer.model.LookUpCategoryNames()  

    newQuizer.view.mainloop()