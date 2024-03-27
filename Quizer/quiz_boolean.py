import customtkinter as ctk
import config as cf


class BooleanQuizGUI(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    # WIDGETS ---------------------------------------------------------------#
    
        ctk.CTkLabel(self,
            text = "True / False Quiz",            
            font = (cf.FONT_FAMILY, cf.FONT_SIZE+4, cf.FONT_TYPE),
            bg_color = cf.LABEL_BG,
            width = cf.WINDOW_WIDTH,
            height = cf.LABEL_HEIGHT
        ).grid(row = 0, column = 0,
            pady = (0, 15), columnspan = 2
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

        self.buttonTrue = ctk.CTkButton(self,
            text = "True",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width = cf.BOTTON_WIDTH,
            height = cf.BOTTON_HEIGHT
        )
        self.buttonTrue.grid(row = 2, column = 0, pady = (0, 10))

        self.buttonFalse = ctk.CTkButton(self,
            text = "False",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width = cf.BOTTON_WIDTH,
            height = cf.BOTTON_HEIGHT
        )
        self.buttonFalse.grid(row = 2, column = 1, pady = (0, 10))

        self.homeButton = ctk.CTkButton(self,
            text = "Back to Home",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width = cf.BOTTON_WIDTH,
            height = cf.BOTTON_HEIGHT
        )
        self.homeButton.grid(row = 3, column = 0, 
            pady = 10, columnspan = 2
        )