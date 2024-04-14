import customtkinter as ctk
from PIL import Image
import config as cf


class HomeGUI(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        logoIMG = ctk.CTkImage(
            dark_image=Image.open("Quizer/rsc/logo.png"),
            size=(250, 100)
        )


        # WIDGETS ---------------------------------------------------------------#

        ctk.CTkLabel(self,
            image = logoIMG,
            fg_color = cf.LABEL_FG,
            width = cf.LOGO_FRAME_WIDTH,
            height = cf.LOGO_FRAME_HEIGHT,
            corner_radius = cf.CORNER_RADIUS,
            text = ""
        ).pack(pady = (15, 15))

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