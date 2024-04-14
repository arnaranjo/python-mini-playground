import customtkinter as ctk
from PIL import Image
import config as cf


class AboutGUI(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        aboutIMG = ctk.CTkImage(
            dark_image=Image.open("Quizer/rsc/about.png"),
            size=(250, 100)
        )


        # WIDGETS ---------------------------------------------------------------#

        ctk.CTkLabel(self,
            image = aboutIMG,
            fg_color = cf.LABEL_FG,
            width = cf.WINDOW_WIDTH - cf.WINDOW_QUIZ_MARGIN,
            height = cf.LOGO_FRAME_HEIGHT,
            corner_radius = cf.CORNER_RADIUS,
            text = ""
        ).pack(pady = (15, 15))

        self.aboutText = ctk.CTkTextbox(self,
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, "bold"),
            width = cf.WINDOW_WIDTH - cf.WINDOW_QUIZ_MARGIN,
            height = cf.WINDOW_ABOUT_HEIGHT,
            corner_radius = cf.CORNER_RADIUS,
        )
        self.aboutText.insert("0.0", cf.ABOUT)
        self.aboutText.pack(pady = (0, 20))

        self.homeButton = ctk.CTkButton(self,
            text = "Back to Home",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width = cf.BOTTON_WIDTH,
            height = cf.BOTTON_HEIGHT
        )
        self.homeButton.pack()