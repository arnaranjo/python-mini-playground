import base64
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
            self.view.SwitchResuls(self.rightAnswers, self.quizNumber)
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