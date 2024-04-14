import customtkinter as ctk
import config as cf
from PIL import Image


class ResultsGUI(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        resultIMG = ctk.CTkImage(
            dark_image=Image.open("Quizer/rsc/result.png"),
            size=(250, 100)
        )


        # WIDGETS ---------------------------------------------------------------#

        ctk.CTkLabel(self,
            image = resultIMG,
            fg_color = cf.LABEL_FG,
            text_color = cf.TEXT_COLOR,
            width = cf.LOGO_FRAME_WIDTH,
            height = cf.LOGO_FRAME_HEIGHT,
            corner_radius = cf.CORNER_RADIUS,
            text = ""
        ).pack(pady = (15, 15))

        self.resultLabel = ctk.CTkLabel(self,
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            fg_color = cf.LABEL_FG,
            text_color = cf.TEXT_COLOR,
            width = cf.LABEL_WIDTH,
            height = cf.RESULT_LABEL_HEIGHT,
            corner_radius = cf.CORNER_RADIUS
        )
        self.resultLabel.pack(pady= (0, 15))

        self.homeButton = ctk.CTkButton(self,
            text= "Back to Home",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width= cf.BOTTON_WIDTH,
            height = cf.BOTTON_HEIGHT,
        )
        self.homeButton.pack(pady= (0, 15))