import customtkinter as ctk

WINDOW_WIDTH = 450

FONT_FAMILY = "arial"
FONT_SIZE = 16
FONT_TYPE = "normal"

LABEL_WIDTH = 120
LABEL_HEIGHT = 40
BOTTON_HEIGHT = 40
BOTTON_WIDTH = 180

LABEL_BG = "#6D597A"


class MultipleQuizGUI(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        
    # WIDGETS ---------------------------------------------------------------#
    
        ctk.CTkLabel(self,
            text = "Multiple Answer Quiz",            
            font = (FONT_FAMILY, FONT_SIZE+4, FONT_TYPE),
            bg_color = LABEL_BG,
            width= WINDOW_WIDTH,
            height = LABEL_HEIGHT
        ).grid(row= 0, column= 0,
            pady= (0, 15), columnspan= 2
        )

        self.textQuiz = ctk.CTkTextbox(self,
            font = (FONT_FAMILY, FONT_SIZE, "bold"),
            width= 400,
            height= 250,
            corner_radius= 15
        )
        self.textQuiz.grid(row= 1, column= 0,
            pady= (0, 15), columnspan= 2
        )
        self.textQuiz.insert("0.0", "Some example text!\n")

        self.buttonA = ctk.CTkButton(self,
            text= "A",
            font = (FONT_FAMILY, FONT_SIZE, FONT_TYPE),
            width= BOTTON_WIDTH,
            height = BOTTON_HEIGHT
        )
        self.buttonA.grid(row= 2, column= 0, pady= (0, 10))

        self.buttonB = ctk.CTkButton(self,
            text= "B",
            font = (FONT_FAMILY, FONT_SIZE, FONT_TYPE),
            width= BOTTON_WIDTH,
            height = BOTTON_HEIGHT
        )
        self.buttonB.grid(row= 2, column= 1, pady= (0, 10))

        self.buttonC = ctk.CTkButton(self,
            text= "C",
            font = (FONT_FAMILY, FONT_SIZE, FONT_TYPE),
            width= BOTTON_WIDTH,
            height = BOTTON_HEIGHT
        )
        self.buttonC.grid(row= 3, column= 0, pady= (0, 10))

        self.buttonD = ctk.CTkButton(self,
            text= "D",
            font = (FONT_FAMILY, FONT_SIZE, FONT_TYPE),
            width= BOTTON_WIDTH,
            height = BOTTON_HEIGHT
        )
        self.buttonD.grid(row= 3, column= 1, pady= (0, 10))

        self.homeButton = ctk.CTkButton(self,
            text= "Back to Home",
            font = (FONT_FAMILY, FONT_SIZE, FONT_TYPE),
            width= 200,
            height = 50
        )
        self.homeButton.grid(row= 4, column= 0, 
            pady= 10, columnspan= 2
        )
        
        self.buttonList = [
            self.buttonA,
            self.buttonB,
            self.buttonC,
            self.buttonD
        ]
