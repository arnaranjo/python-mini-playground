from ccypher import CCypher
from gui import CCypherGUI

class CCypherController:
    def __init__(self, Model, View):
        
        self.model = Model
        self.view = View

        self.result = ""

    def Execute(self):
        try:
            if self.view.varRadio.get() == 0:
                self.result = self.model.Encrypt(
                    self.view.textEntry.get(),
                    self.view.varStep.get()
                )
                self.view.resultLabel.config(text = self.result)

            elif self.view.varRadio.get() == 1:
                self.result = self.model.Decrypt(
                self.view.textEntry.get(),
                self.view.varStep.get()
                )
                self.view.resultLabel.config(text = self.result)

        except:
            self.view.textError()

#--------------------------------------------------------------#

if __name__ == "__main__":
    newCypher = CCypher()
    newController = CCypherController(newCypher, None)
    newGUI = CCypherGUI(newController)
    newController.view = newGUI
    newGUI.mainloop()