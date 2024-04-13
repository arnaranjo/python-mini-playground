import customtkinter as ctk
import config as cf


class BooleanQuizGUI(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    # WIDGETS ---------------------------------------------------------------#
    
        ctk.CTkLabel(self,
            text = "True / False Quiz",            
            font = (cf.FONT_FAMILY, cf.FONT_SIZE_TITLE, cf.FONT_TYPE),
            fg_color = cf.LABEL_FG,
            text_color = cf.TEXT_COLOR,
            width = cf.WINDOW_WIDTH,
            height = cf.LABEL_HEIGHT
        ).pack(pady = (0, 20))

        self.textQuiz = ctk.CTkTextbox(self,
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, "bold"),
            width = cf.WINDOW_WIDTH - cf.WINDOW_QUIZ_MARGIN,
            height = cf.WINDOW_QUIZ_HEIGHT,
            corner_radius = cf.LOGO_CORNER_RADIUS
        )
        self.textQuiz.pack(pady = (0, 20))

        self.buttonTrue = ctk.CTkButton(self,
            text = "True",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width = cf.WINDOW_WIDTH - cf.WINDOW_QUIZ_MARGIN,
            height = cf.BOTTON_HEIGHT
        )
        self.buttonTrue.pack(pady = (0, 10))

        self.buttonFalse = ctk.CTkButton(self,
            text = "False",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width = cf.WINDOW_WIDTH - cf.WINDOW_QUIZ_MARGIN,
            height = cf.BOTTON_HEIGHT
        )
        self.buttonFalse.pack(pady = (0, 20))

        self.homeButton = ctk.CTkButton(self,
            text = "Back to Home",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width = cf.BOTTON_WIDTH,
            height = cf.BOTTON_HEIGHT
        )
        self.homeButton.pack()