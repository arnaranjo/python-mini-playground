import customtkinter as ctk
import config as cf


class ResultsGUI(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # WIDGETS ---------------------------------------------------------------#

        ctk.CTkLabel(self,
            text="Hello from results"
        ).pack(pady= (0, 15))

        self.resultLabel = ctk.CTkLabel(self,
            text="Results"
        )
        self.resultLabel.pack(pady= (0, 15))

        self.homeButton = ctk.CTkButton(self,
            text= "Back to Home",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width= cf.BOTTON_WIDTH,
            height = cf.BOTTON_HEIGHT
        )
        self.homeButton.pack(pady= (0, 15))