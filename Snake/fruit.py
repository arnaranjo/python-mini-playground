from turtle import Turtle
from random import randint

class Fruit(Turtle):
    def __init__(self, screenWidth, screenHeight, fruitColor):
        super().__init__()
        self.fruitColor = fruitColor
        self.maxWidth = screenWidth
        self.maxHeight = screenHeight   
        self.SetNewFruit()

    def GenPosition(self):
        if self.isvisible:
            self.showturtle()
        newX = randint((-self.maxWidth/2 + 100),(self.maxWidth/2 - 100))
        newY = randint((-self.maxHeight/2 + 100),(self.maxHeight/2 - 100))
        self.setpos(newX, newY)

    def SetNewFruit(self):
        self.shape("circle")     
        self.shapesize(0.5,0.5)   
        self.color(self.fruitColor)
        self.penup()
        self.GenPosition()

    def RemoveFruit(self):
        self.reset()
        self.hideturtle()