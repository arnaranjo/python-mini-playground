import customtkinter as ctk
import config as cf


class HomeGUI(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        ctk.CTkLabel(self, text = "Hello from home").pack(pady = (0, 15))

        #TODO: Quiz logo with the light and dark colours.
        self.settingsButton = ctk.CTkButton(self,
            text = "Settings",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width = cf.BOTTON_WIDTH,
            height = cf.BOTTON_HEIGHT
        )
        self.settingsButton.pack(pady = (0, 15))

        self.startButton = ctk.CTkButton(self,
            text = "Start Quiz!",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width = cf.BOTTON_WIDTH,
            height = cf.BOTTON_HEIGHT
        )
        self.startButton.pack(pady = (0, 15))

        self.quitButton = ctk.CTkButton(self,
            text = "Exit",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width = cf.BOTTON_WIDTH,
            height = cf.BOTTON_HEIGHT
        )
        self.quitButton.pack(pady = (0, 15))