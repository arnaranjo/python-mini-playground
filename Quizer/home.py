import customtkinter as ctk

FONT_FAMILY = "arial"
FONT_SIZE = 16
FONT_TYPE = "normal"

BOTTON_HEIGHT = 50
BOTTON_WIDTH = 200


class HomeGUI(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        ctk.CTkLabel(self, text="Hello from home").pack(pady= (0, 15))

        self.settingsButton = ctk.CTkButton(self,
            text= "Settings",
            font = (FONT_FAMILY, FONT_SIZE, FONT_TYPE),
            width= BOTTON_WIDTH,
            height = BOTTON_HEIGHT
        )
        self.settingsButton.pack(pady= (0, 15))

        self.startButton = ctk.CTkButton(self,
            text= "Start Quiz!",
            font = (FONT_FAMILY, FONT_SIZE, FONT_TYPE),
            width= BOTTON_WIDTH,
            height = BOTTON_HEIGHT
        )
        self.startButton.pack(pady= (0, 15))
