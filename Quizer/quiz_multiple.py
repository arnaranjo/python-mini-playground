import customtkinter as ctk
import config as cf


class MultipleQuizGUI(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


    # WIDGETS ---------------------------------------------------------------#
    
        ctk.CTkLabel(self,
            text = "Multiple Answer Quiz",
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
            corner_radius = cf.CORNER_RADIUS
        )
        self.textQuiz.pack(pady = (0, 20))

        self.buttonA = ctk.CTkButton(self,
            text = "A",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width = cf.WINDOW_WIDTH - cf.WINDOW_QUIZ_MARGIN,
            height = cf.BOTTON_HEIGHT
        )
        self.buttonA.pack(pady = (0, 10))

        self.buttonB = ctk.CTkButton(self,
            text = "B",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width = cf.WINDOW_WIDTH - cf.WINDOW_QUIZ_MARGIN,
            height = cf.BOTTON_HEIGHT
        )
        self.buttonB.pack(pady = (0, 10))

        self.buttonC = ctk.CTkButton(self,
            text = "C",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width = cf.WINDOW_WIDTH - cf.WINDOW_QUIZ_MARGIN,
            height = cf.BOTTON_HEIGHT
        )
        self.buttonC.pack(pady = (0, 10))

        self.buttonD = ctk.CTkButton(self,
            text = "D",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width = cf.WINDOW_WIDTH - cf.WINDOW_QUIZ_MARGIN,
            height = cf.BOTTON_HEIGHT
        )
        self.buttonD.pack(pady = (0, 20))

        self.homeButton = ctk.CTkButton(self,
            text = "Back to Home",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width = cf.BOTTON_WIDTH,
            height = cf.BOTTON_HEIGHT
        )
        self.homeButton.pack()

        self.buttonList = [
            self.buttonA,
            self.buttonB,
            self.buttonC,
            self.buttonD
        ]