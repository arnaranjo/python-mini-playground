import customtkinter as ctk

FONT_FAMILY = "arial"
FONT_SIZE = 16
FONT_TYPE = "normal"

BOTTON_HEIGHT = 50
BOTTON_WIDTH = 200


class ResultsGUI(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        ctk.CTkLabel(self,
            text="Hello from results"
        ).pack(pady= (0, 15))

        self.resultLabel = ctk.CTkLabel(self,
            text="Results"
        )
        self.resultLabel.pack(pady= (0, 15))

        self.homeButton = ctk.CTkButton(self,
            text= "Back to Home",
            font = (FONT_FAMILY, FONT_SIZE, FONT_TYPE),
            width= BOTTON_WIDTH,
            height = BOTTON_HEIGHT
        )
        self.homeButton.pack(pady= (0, 15))