from turtle import Turtle

class Display():
    def __init__(self, topLimit, bottomLimit, leftLimit, rightLimit, displayColor):
        
        self.displayColor = displayColor

        self.topLimit = topLimit
        self.bottomLimit = bottomLimit
        self.leftLimit = leftLimit
        self.rightLimit = rightLimit

        self.newPen = Turtle()
        self.newScorePen = Turtle()

        self.score = 0

        self.SetDisplay()
        self.SetText()
    
    def SetDisplay(self):
        self.newPen.hideturtle()
        self.newPen.color(self.displayColor)
        self.newPen.penup()
        self.newPen.goto(self.leftLimit, self.topLimit)
        self.newPen.pendown()
        self.newPen.goto(self.rightLimit, self.topLimit)
        self.newPen.goto(self.rightLimit, self.bottomLimit)
        self.newPen.goto(self.leftLimit, self.bottomLimit)
        self.newPen.goto(self.leftLimit, self.topLimit)

    def SetText(self):
        self.newScorePen.hideturtle()
        self.newScorePen.color(self.displayColor)
        self.newScorePen.penup()
        self.newScorePen.goto(self.leftLimit, self.topLimit + 10)
        self.newScorePen.pendown()
        self.newScorePen.write(
            arg = f"Score: {self.score}",
            align = "left",
            font = ("courier", 16, "normal")
        )
    
    def Update(self):
        self.newScorePen.clear()
        self.SetText()

    def IncreaseScore(self):
        self.score += 1
        self.Update()
    
    def ResetScore(self):
        self.score = 0
        self.Update()