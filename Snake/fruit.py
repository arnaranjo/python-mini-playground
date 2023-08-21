from turtle import Turtle
from random import randint

class Fruit():
    def __init__(self, screenWidth, screenHeight):

        self.maxWidth = screenWidth
        self.maxHeight = screenHeight
        self.currentFruit = None    
        self.SetNewFruit()

    def GenPosition(self):
        newX = randint((-self.maxWidth/2 + 100),(self.maxWidth/2 - 100))
        newY = randint((-self.maxHeight/2 + 100),(self.maxHeight/2 - 100))
        self.currentFruit.setpos(newX, newY)

    def SetNewFruit(self):
        self.currentFruit = Turtle("circle")        
        self.currentFruit.color("blue")
        self.currentFruit.penup()
        self.GenPosition()