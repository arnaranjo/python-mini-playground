from root import RootGUI
from quizer import QuizerModel


class QuizerController():
    def __init__(self, View: RootGUI, Model :QuizerModel): 
        self.view = View
        self.model = Model
        self.quizNumber = 0

        self.questionsRequested = []

    def RequestQuestions(self, parameters):
        self.model.finalParameters = parameters
        self.questionsRequested = self.model.LookUpQuestions()

    def BeginQuiz(self, answer):
        # TODO: Apply encode to the answer.
        # TODO: Implement the count system.
        if answer == self.questionsRequested[self.quizNumber]["correct_answer"]:
            print("OK")            
        else:
            print("FAIL")

        self.quizNumber += 1 
                   
        if self.quizNumber >= len(self.questionsRequested):
            #TODO Implement the final and reset of the quiz
            self.view.SwitchHome()
            self.quizNumber = 0

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