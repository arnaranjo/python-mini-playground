import customtkinter as ctk
import config as cf


class SettingsGUI(ctk.CTkFrame):
    def __init__(self, master,  **kwargs):
        super().__init__(master, **kwargs)

        self.lightTheme = False

    # WIDGETS ---------------------------------------------------------------#
    
        ctk.CTkLabel(self,
            text = "Quiz Settings",            
            font = (cf.FONT_FAMILY, cf.FONT_SIZE+4, cf.FONT_TYPE),
            bg_color = cf.LABEL_BG,
            width = cf.WINDOW_WIDTH,
            height = cf.LABEL_HEIGHT
        ).grid(
            row = 0, column = 0,
            pady = (0, 15), columnspan = 3
        )

        ctk.CTkLabel(self,
            text = "Nº Questions",            
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            bg_color = cf.LABEL_BG,
            width = cf.LABEL_WIDTH,
            height = cf.LABEL_HEIGHT
        ).grid(
            row = 1, column = 0,
            pady = (0, 15), padx = 10
        )

        self.numberSelectorLabel = ctk.CTkLabel(self,
            text = "27",            
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            bg_color = cf.LABEL_BG,
            width = 50,
            height = cf.LABEL_HEIGHT
        )
        self.numberSelectorLabel.grid(
            row = 1, column = 1,
            pady = (0, 15), padx = 10
        )

        self.numberSelector = ctk.CTkSlider(self,
            from_ = 5,
            to = 50,
            number_of_steps = 45,
            command = self.SliderEvent
        )
        self.numberSelector.grid(
            row = 1, column = 2,
            pady = (0, 15), padx = 10
        )

        ctk.CTkLabel(self,
            text = "Category",            
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            bg_color = cf.LABEL_BG,
            width = cf.LABEL_WIDTH,
            height = cf.LABEL_HEIGHT
        ).grid(
            row = 2, column = 0,
            pady = (0, 15), padx = 10
        )

        self.categoryBox = ctk.CTkComboBox(self,
            height = cf.LABEL_HEIGHT           
        )
        self.categoryBox.grid(
            row = 2, column = 1, columnspan = 2,
            pady = (0, 15), padx = 10, sticky = 'ew'
        )
        self.categoryBox.set("Any Category")

        ctk.CTkLabel(self,
            text = "Difficulty",            
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            bg_color = cf.LABEL_BG,
            width = cf.LABEL_WIDTH,
            height = cf.LABEL_HEIGHT
        ).grid(
            row = 3, column = 0,
            pady = (0, 15), padx = 10
        )

        self.difficultyBox = ctk.CTkComboBox(self,
            height = cf.LABEL_HEIGHT,
            values = ["Any Difficulty", "Easy", "Medium", "Hard"]       
        )
        self.difficultyBox.grid(
            row = 3, column = 1, columnspan = 2,
            pady = (0, 15), padx = 10, sticky ='ew'
        )
        self.difficultyBox.set("Any Difficulty")

        ctk.CTkLabel(self,
            text = "Type",            
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            bg_color = cf.LABEL_BG,
            width = cf.LABEL_WIDTH,
            height = cf.LABEL_HEIGHT
        ).grid(
            row = 4, column = 0,
            pady = (0, 15), padx = 10
        )

        self.typeBox = ctk.CTkComboBox(self,
            height = cf.LABEL_HEIGHT,
            values = ["Any Type", "Multiple", "True/False"]          
        )
        self.typeBox.grid(
            row = 4, column = 1, columnspan = 2,
            pady = (0, 15), padx = 10, sticky = 'ew'
        )
        self.typeBox.set("Any Type")

        self.saveButton = ctk.CTkButton(self,
            text = "Save Settings",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width = cf.BOTTON_WIDTH,
            height = cf.BOTTON_HEIGHT
        )
        self.saveButton.grid(
            row = 5, column = 0, 
            pady = 10, columnspan = 3
        )

        self.homeButton = ctk.CTkButton(self,
            text = "Back to Home",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width = cf.BOTTON_WIDTH,
            height = cf.BOTTON_HEIGHT
        )
        self.homeButton.grid(
            row = 6, column = 0, 
            pady = 10, columnspan = 3
        )

        #TODO: Window with the credits
        self.infoButton = ctk.CTkButton(self,
            text = "Credits",
            font = (cf.FONT_FAMILY, cf.FONT_SIZE, cf.FONT_TYPE),
            width = cf.BOTTON_WIDTH,
            height = cf.BOTTON_HEIGHT
        )
        self.infoButton.grid(
            row = 7, column = 0, 
            pady = 10, columnspan = 3
        )

    # METHODS ---------------------------------------------------------------#

    def SliderEvent(self, value):
        self.numberSelectorLabel.configure(
            text= str(int(value))
        )


    def GetSelections(self, categories):
        parameters = {}

        # Number of questions selected.
        parameters["amount"] = int(self.numberSelector.get())

        # Category selection.
        if self.categoryBox.get() != "Any Category":
            for category in categories:
                if category["name"] == self.categoryBox.get():
                    parameters["category"] = category["id"]
                    
        elif self.categoryBox.get() == "Any Category" \
            and "category" in parameters:
            parameters.pop("category")

        # Difficulty selection.
        if self.difficultyBox.get() != "Any Difficulty":
            if self.difficultyBox.get() == "Easy":
                parameters["difficulty"] = "easy"

            elif self.difficultyBox.get() == "Medium":
                parameters["difficulty"] = "medium"

            elif self.difficultyBox.get() == "Hard":
                parameters["difficulty"] = "hard"

        elif self.difficultyBox.get() == "Any Difficulty" \
            and "difficulty" in parameters:
            parameters.pop("difficulty")

        # Type selection.
        if self.typeBox.get() != "Any Type":
            if self.typeBox.get() == "Multiple":
                parameters["type"] = "multiple"

            elif self.typeBox.get() == "True/False":
                parameters["type"] = "boolean"
                
        elif self.typeBox.get() == "Any Type" \
            and "type" in parameters:
            parameters.pop("type")

        # List of parameters completed to request the questions.
        return parameters