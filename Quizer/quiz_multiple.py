import customtkinter as ctk
import config as cf


class MultipleQuizGUI(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
    # WIDGETS ---------------------------------------------------------------#
    
        ctk.CTkLabel(self,
            text = "Multiple Answer Quiz",            
            font = (cf.FONT_FAMILY, cf.FONT_SIZE + 4, cf.FONT_TYPE),
            bg_color = cf.LABEL_BG,
            width = cf.WINDOW_WIDTH,
            height = cf.LABEL_HEIGHT
        ).grid(row = 0, column= 0,
            pady = (0, 15), columnspan= 2
        )

        self.textQuiz = ctk.CTkTextbox(self,
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, "bold"),
            width = cf.WINDOW_WIDTH - 50,
            height = 250,
            corner_radius = 15
        )
        self.textQuiz.grid(row = 1, column = 0,
            pady = (0, 15), columnspan = 2
        )

        self.buttonA = ctk.CTkButton(self,
            text = "A",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width = cf.BOTTON_WIDTH,
            height = cf.BOTTON_HEIGHT
        )
        self.buttonA.grid(row = 2, column = 0, pady = (0, 10))

        self.buttonB = ctk.CTkButton(self,
            text = "B",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width = cf.BOTTON_WIDTH,
            height = cf.BOTTON_HEIGHT
        )
        self.buttonB.grid(row = 2, column = 1, pady = (0, 10))

        self.buttonC = ctk.CTkButton(self,
            text = "C",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width = cf.BOTTON_WIDTH,
            height = cf.BOTTON_HEIGHT
        )
        self.buttonC.grid(row = 3, column = 0, pady = (0, 10))

        self.buttonD = ctk.CTkButton(self,
            text = "D",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width = cf.BOTTON_WIDTH,
            height = cf.BOTTON_HEIGHT
        )
        self.buttonD.grid(row= 3, column= 1, pady= (0, 10))

        self.homeButton = ctk.CTkButton(self,
            text = "Back to Home",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width = 200,
            height = 50
        )
        self.homeButton.grid(row = 4, column = 0, 
            pady = 10, columnspan = 2
        )
        
        self.buttonList = [
            self.buttonA,
            self.buttonB,
            self.buttonC,
            self.buttonD
        ]
